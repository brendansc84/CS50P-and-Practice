def main():
    dollars = dollars_float(input("How much was the meal? ").strip())
    percent = percent_float(input("What percentage would you like to tip? ").strip())
    tip = dollars * percent
    print(f"Leave $ {tip:.2f}")

def dollars_float(d):
    d = float(d)
    return d

def percent_float(p):
    p = float(p) / 100
    return p

main()