import re

name = input("What is your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"Hello, {name}")

# in regex . means "any character"
# the + means "one or more of the preceding character"
# the * means "zero or more of the preceding character"
# the \ means "escape the following character"
