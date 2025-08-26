import sys
import csv

def main():
    
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    inpath, outpath = sys.argv[1], sys.argv[2]

    try:
        with open(inpath, encoding="utf-8-sig") as infile, \
            open(outpath, "w", newline="") as outfile:
            reader = csv.DictReader(infile)
            writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
            writer.writeheader()

            for row in reader:
                name = row["name"]
                last, first = (p.strip() for p in name.split(",", 1))
                writer.writerow({
                    "first": first,
                    "last": last,
                    "house": row["house"].strip()
                })
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
