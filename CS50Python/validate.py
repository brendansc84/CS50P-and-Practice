import re

email = input("What's your email? ").strip()

if re.search(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|edu|org|gov|net|ca|uk)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")