'''pizzas = ["Cheese", "Meat Lover's", "BBQ Chicken"]
friends_pizzas = pizzas[:]

pizzas.append("pepperoni")
friends_pizzas.append("hawaiian")

for pizza in pizzas:
    print(f"I love {pizza} pizza!")

print("\nI really fucking love pizza.")

print("My fave Pizzas are:")
for pizza in pizzas:
    print(pizza.title())


print("\nMy friend's fave pizzas are:")
for friends_pizza in friends_pizzas:
    print(friends_pizza.title())'''

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")