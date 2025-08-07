def armor():
    budget = 0
    gear = {
        "helmet": 50,
        "armor": 100,
        "boots": 25,
        "shield": 75
    }

    while True:
        text = input("Item: ").lower()
        if text == "done":
            break

        if text in gear:
            budget += gear[text]
        else:
            print("Not a valid item")

    print(f"Total budget: ${budget:.2f}")
if __name__ == "__main__":
    armor()