prompt = "\nPlease enter the name of a city you have visited."
prompt += "\n(enter 'quit' when you are finished): "

while True:
    city = input(prompt).lower()

    if city == 'quit':
        break
    elif city == 'edmonton':
        print(f"Eww, fuck {city.title()}! Good thing you left.")
    else:
        print(f"I'd love to go to {city.title()}!")