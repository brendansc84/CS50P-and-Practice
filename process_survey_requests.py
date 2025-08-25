import os, re, json, zipfile, sys
from pathlib import Path
import win32com.client
import pythoncom
from contextlib import contextmanager

def runtime_dir() -> Path:
    # When frozen (PyInstaller), write beside the EXE; otherwise beside the .py
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent
    return Path(__file__).parent

RUNTIME_DIR = runtime_dir()
LOCK_PATH = RUNTIME_DIR / "process_sr.lock"                   # lock beside the exe/py
LOG_PATH  = RUNTIME_DIR / "processed_sr_entryids.json"        # seen cache beside the exe/py

@contextmanager
def single_instance_lock():
    try:
        fd = os.open(LOCK_PATH, os.O_CREAT | os.O_EXCL | os.O_RDWR)
    except FileExistsError:
        print("Another run is in progress. Exiting.")
        raise SystemExit(0)
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
MAIL_FOLDER = "Inbox"  # optional; see resolve_mail_folder if you want subfolders
SR_SUBJECT_PATTERN = re.compile(r"\bSR\d{8,}\b", re.I)
MAX_NAME = 150

# UTILITIES
INVALID_FS_CHARS = r'<>:"/\|?*'
TRANS = str.maketrans({c: " " for c in INVALID_FS_CHARS})

PREFIX_RE = re.compile(r'^\s*((RE|FW|FWD)\s*:)+\s*', re.I)

def strip_fw_re(s: str) -> str:
    return PREFIX_RE.sub('', s or '')

def extract_sr_id(s: str) -> str | None:
    m = SR_SUBJECT_PATTERN.search(s or '')
    return m.group(0).upper() if m else None

def safe_folder_name(subject: str) -> str:
    clean = subject.translate(TRANS).strip()
    clean = re.sub(r"\s+", " ", clean)
    return clean[:MAX_NAME].rstrip(" .")

def safe_file_name(name: str) -> str:
    # Strip any path components and sanitize for Windows
    base = Path(name).name.translate(TRANS).strip().rstrip(" .")
    base = re.sub(r"\s+", " ", base)
    if not base:
        base = "attachment"
    return base[:MAX_NAME]

def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)

def unique_path(p: Path) -> Path:
    """Return a unique path (adds _2, _3, ... before suffix if needed)."""
    if not p.exists():
        return p
    stem, suffix = p.stem, p.suffix
    i = 2
    while True:
        cand = p.with_name(f"{stem}_{i}{suffix}")
        if not cand.exists():
            return cand
        i += 1

def secure_extract_member(zf: zipfile.ZipFile, member: zipfile.ZipInfo, dest: Path):
    """
    Safely extract a single ZipInfo to dest, avoiding zip-slip.
    Returns path written or None if skipped (dir or unsafe).
    """
    if member.is_dir():
        return None
    fname = Path(member.filename).name  # drop folders in zip
    if not fname:
        return None
    out_path = unique_path(dest / safe_file_name(fname))
    try:
        out_path_resolved = out_path.resolve()
        dest_resolved = dest.resolve()
        if dest_resolved not in out_path_resolved.parents and out_path_resolved != dest_resolved:
            return None
    except Exception:
        pass
    with zf.open(member) as src, open(out_path, "wb") as dst:
        dst.write(src.read())
    return out_path

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
    msg_path = unique_path(dest_folder / f"{fname}.msg")
    mail.SaveAs(str(msg_path), 3)  # 3 = .msg
    return msg_path

def save_attachments(mail, dest_folder: Path):
    """
    Saves all attachments. For .zip files:
      - saves the zip
      - extracts its contents into dest_folder
      - deletes the zip file after extraction
    Returns list of saved attachment file paths (post-dedup), excluding extracted files.
    """
    saved = []
    for att in mail.Attachments:
        raw_name = str(att.FileName) or "attachment"
        clean_name = safe_file_name(raw_name)
        save_path = unique_path(dest_folder / clean_name)
        try:
            att.SaveAsFile(str(save_path))
            if clean_name.lower().endswith(".zip"):
                try:
                    with zipfile.ZipFile(save_path, "r") as zf:
                        for member in zf.infolist():
                            secure_extract_member(zf, member, dest_folder)
                except zipfile.BadZipFile:
                    print(f"  ! Corrupt zip (saved but not extracted): {save_path.name}")
                finally:
                    try:
                        save_path.unlink(missing_ok=True)
                    except Exception as e:
                        print(f"  ! Failed to delete zip {save_path.name}: {e}")
            else:
                saved.append(str(save_path))
        except Exception as e:
            print(f"  ! Failed to save attachment {clean_name}: {e}")
    return saved

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
    folder = outlook.GetDefaultFolder(OL_FOLDER_INBOX)  # or resolve_mail_folder(outlook, MAIL_FOLDER)

    items = folder.Items
    items.Sort("[ReceivedTime]", True)

    seen = load_log()
    processed = 0

    for mail in items:
        if getattr(mail, "Class", None) != 43:  # 43 = MailItem
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

        clean_subject = strip_fw_re(subject)
        sr_id = extract_sr_id(clean_subject)
        dest_name = sr_id if sr_id else safe_folder_name(clean_subject)
        dest = Path(BASE_DIR) / dest_name
        ensure_dir(dest)

        print(f"Processing: {subject} -> [{dest_name}]")

        try:
            save_msg(mail, dest, clean_subject)
        except Exception as e:
            print(f"  ! Failed to save .msg: {e}")

        try:
            saved_non_zips = save_attachments(mail, dest)
            if saved_non_zips:
                print(f"  Saved attachments: {', '.join(Path(p).name for p in saved_non_zips)}")
            else:
                print("  No non-zip attachments saved (zips extracted & deleted, or no attachments).")
        except Exception as e:
            print(f"  ! Failed to handle attachments: {e}")

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
    with single_instance_lock():
        process_folder()
