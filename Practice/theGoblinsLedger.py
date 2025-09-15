def main():
    items = {
        "sword": 50,
        "shield": 35,
        "potion": 10,
        "boots": 25
    }

    while True:
        try:
            item = input("Enter item name (or 'done' to finish): ").strip().lower()
            if item == "done":
                break
            if item not in items:
                print("Item not found.")
                continue
            quantity = int(input("Enter quantity: "))
            if quantity < 1:
                print("Invalid quantity.")
                continue
            total = items[item] * quantity
            print(f"Added {quantity} {item}(s) to your ledger. Total: {total}")
        except ValueError:
            print("Invalid input. Please enter a valid item and quantity.")

if __name__ == "__main__":
    main()