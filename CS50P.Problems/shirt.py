import sys
from PIL import Image, ImageOps

VALID_EXTS = (".jpg", ".jpeg", ".png")

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input_image output_image")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    in_ext = get_ext(input_path)
    out_ext = get_ext(output_path)

    if in_ext not in VALID_EXTS:
        sys.exit("Invalid input")
    if out_ext not in VALID_EXTS:
        sys.exit("Invalid output")
    if in_ext != out_ext:
        sys.exit("Input and output have different extensions")

    try:
        photo = Image.open(input_path)
    except FileNotFoundError:
        sys.exit(f"Could not open {input_path}")

    shirt = Image.open("shirt.png")
    fitted = ImageOps.fit(photo, shirt.size)
    fitted.paste(shirt, mask=shirt)
    fitted.save(output_path)

def get_ext(path: str) -> str:
    dot = path.rfind(".")
    return path[dot:].lower() if dot != -1 else ""

if __name__ == "__main__":
    main()
