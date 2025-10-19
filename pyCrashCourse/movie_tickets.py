total = 0

while True:
    age_str = (input("Welcome to Silverscreen Theaters! (type 'done' for total)\nPlease enter age: ").lower().strip())
    if age_str == 'done':
        break
    age = int(age_str)

    if age < 3:
        total += 0
    elif 3 <= age <= 12:
        total += 10
    else:
        total += 15


print(f"Your total is ${total}")