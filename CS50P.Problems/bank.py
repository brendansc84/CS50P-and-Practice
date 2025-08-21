def main():
    greeting = input("Greeting: ")
    amount = value(greeting)
    print(f"${amount}")

def value(greeting):
    g = greeting.lower()
    if g.startswith("hello"):
        return 0
    elif g.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()