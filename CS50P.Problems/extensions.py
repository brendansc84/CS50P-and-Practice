def main():
    filename = input("File name: ")
    ext = filename.rsplit(".", 1)[-1].lower()
    mime_type = {
        "gif": "image/gif",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "pdf": "application/pdf",
        "txt": "text/plain",
        "zip": "application/zip"
    }
    print(mime_type.get(ext, "application/octet-stream"))

main()
