def main():
    total = 0
    coins = {
        "dollar": 1.00,
        "quarter": 0.25,
        "dime": 0.10,
        "nickel": 0.05,
        "penny": 0.01
    }

    while True:
        text = input("Tip: ").lower()
        if text == "done":
            break

        if text in coins:
            total += coins[text]
        else:
            print("Not a valid coin.")

    print(f"Total: ${total:.2f}")

if __name__ == "__main__":
    main()