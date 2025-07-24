def main():
    time = input("What time is it? ").strip()
    converted = convert(time)
    if 7 <= converted <= 8:
        print("Breakfast time")
    elif 12 <= converted <= 13:
        print("Lunch time")
    elif 18 <= converted <= 19:
        print("Dinner time")
    else:
        print("")


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    return hours + minutes / 60

if __name__ == "__main__":
    main()