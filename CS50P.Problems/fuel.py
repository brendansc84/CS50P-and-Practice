def main():
    fraction = input("Fraction: ")
    percent = convert(fraction)
    print(gauge(percent))

def convert(fraction):
    x, y = fraction.split("/")
    return int(x) / int(y) * 100

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{round(percentage)}%"

if __name__ == "__main__":
    main()
