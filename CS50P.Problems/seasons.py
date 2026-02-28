from datetime import date
import sys
import inflect


def main():
    user_input = input("Date of Birth: ").split("-")
    try:
        year, month, day = map(int, user_input)
        birth_date = date(year, month, day)
    except ValueError:
        sys.exit("Invalid date")
    

if __name__ == "__main__":
    main()