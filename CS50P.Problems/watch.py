import re

PATTERN = re.compile(r"""
    <iframe[^>]*?src\s*=\s*["']
    https?://(?:www\.)?youtube\.com/embed/(?P<id>[A-Za-z0-9_-]{11})
    ["'][^>]*?>
    (?:</iframe>)?
    """, re.VERBOSE)

def main():
    print(parse(input("HTML: ")))

def parse(s):
    m = PATTERN.search(s)
    if m:
        return f"https://youtu.be/{m.group('id')}"
    return None

if __name__ == "__main__":
    main()