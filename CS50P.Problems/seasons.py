from datetime import date


def main():
    month = int(input("Month (1-12): "))
    day = int(input("Day (1-31): "))
    if month == 12 and day >= 21 or month in [1, 2] or month == 3 and day < 20: # Winter
        season = "Winter"
    elif month == 3 and day >= 20 or month in [4,5] or month == 6 and day < 21: # Spring
        season = "Spring"
    elif month == 6 and day >= 21 or month in [7,8] or month == 9 and day < 22: # Summer
        season = "Summer"
    else: # Fall
        season = "Fall"
    print(f"{season}")


if __name__ == "__main__":
    main()