import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    # the gd file type issue
    if not filename.lower().endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    count = 0
    for line in lines:
        stripped = line.lstrip()
        if stripped == "" or stripped.startswith("#"):
            continue
        count += 1

    print(count)

if __name__ == "__main__":
    main()