import os, re, json, time, zipfile
from pathlib import Path
import win32com.client
import pythoncom
from contextlib import contextmanager

LOCK_PATH = Path(__file__).with_suffix(".lock")

@contextmanager
def single_instance_lock():
    try:
        fd = os.open(LOCK_PATH, os.O_CREAT | os.O_EXCL | os.O_RDWR)
    except FileExistsError:
        print("Another run is in progress. Exiting.")
        return
    try:
        yield
    finally:
        try:
            os.close(fd)
            LOCK_PATH.unlink(missing_ok=True)
        except Exception:
            pass


# CONFIG
BASE_DIR = r"\\CA0002-PPFSS01\workgroup\1566\active\156660046\Kearl\Survey Requests"
MAIL_FOLDER = "Inbox"
SR_SUBJECT_PATTERN = re.compile(r"\bSR\d{8,}\b", re.I)
LOG_PATH = Path(__file__).with_name("processed_sr_entryids.json")
MAX_NAME = 150

# UTILITIES
INVALID_FS_CHARS = r'<>:"/\|?*'
TRANS = str.maketrans({c: " " for c in INVALID_FS_CHARS})

def safe_folder_name(subject: str) -> str:
    clean = subject.translate(TRANS).strip()
    clean = re.sub(r"\s+", " ", clean)
    return clean[:MAX_NAME].rstrip(" .")

def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)

def load_log() -> set[str]:
    if LOG_PATH.exists():
        try:
            return set(json.loads(LOG_PATH.read_text(encoding="utf-8")))
        except Exception:
            return set()
    return set()

def save_log(seen: set[str]):
    LOG_PATH.write_text(json.dumps(sorted(seen)), encoding="utf-8")

def save_msg(mail, dest_folder: Path, subject: str):
    fname = safe_folder_name(subject) or "message"
    msg_path = dest_folder / f"{fname}.msg"
    mail.SaveAs(str(msg_path), 3)
    return msg_path

def save_and_extract_zips(mail, dest_folder: Path):
    extracted = []
    for att in mail.Attachments:
        name = str(att.FileName)
        if name.lower().endswith(".zip"):
            zip_path = dest_folder / name
            att.SaveAsFile(str(zip_path))
            with zipfile.ZipFile(zip_path, "r") as zf:
                for member in zf.infolist():
                    if member.is_dir():
                        continue
                    fname = Path(member.filename).name
                    out_path = dest_folder / fname
                    with zf.open(member) as src, open(out_path, "wb") as dst:
                        dst.write(src.read())
            extracted.append(str(zip_path))
    return extracted

OL_FOLDER_INBOX = 6

def resolve_mail_folder(namespace, path: str):
    folder = namespace.GetDefaultFolder(OL_FOLDER_INBOX)

    norm = path.strip().strip("\\")
    if norm.lower() == "inbox":
        return folder

    parts = norm.split("\\")
    if parts and parts[0].lower() == "inbox":
        parts = parts[1:]

    for part in parts:
        folder = folder.Folders.Item(part)
    return folder

# MAIN
def process_folder():
    pythoncom.CoInitialize()
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    
    folder = outlook.GetDefaultFolder(6)

    items = folder.Items
    items.Sort("[ReceivedTime]", True)

    seen = load_log()
    processed = 0

    for mail in items:
        if getattr(mail, "Class", None) != 43:
            continue

        if getattr(mail, "UnRead", False) is False:
            continue

        try:
            subject = str(mail.Subject)
            entry_id = str(mail.EntryID)
        except Exception:
            continue

        if entry_id in seen:
            continue
        if not SR_SUBJECT_PATTERN.search(subject):
            continue

        print(f"Processing: {subject}")

        dest = Path(BASE_DIR) / safe_folder_name(subject)
        ensure_dir(dest)

        try:
            save_msg(mail, dest, subject)
        except Exception as e:
            print(f"  ! Failed to save .msg: {e}")

        try:
            zips = save_and_extract_zips(mail, dest)
            if zips:
                print(f"  Extracted: {', '.join(Path(z).name for z in zips)}")
        except Exception as e:
            print(f"  ! Failed to handle zips: {e}")

        try:
            mail.UnRead = False
            mail.Save()
        except Exception:
            pass

        seen.add(entry_id)
        processed += 1

    save_log(seen)
    print(f"Done. Processed {processed} message(s).")

if __name__ == "__main__":
    process_folder()
