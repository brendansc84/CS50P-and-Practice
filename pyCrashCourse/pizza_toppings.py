prompt = "\nWhat toppings would you like on your pizza?"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    topping = input(prompt)

    if topping.lower() == 'quit':
        break
    else:
        print(f"{topping.title()} has been added!")