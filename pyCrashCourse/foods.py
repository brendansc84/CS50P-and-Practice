my_foods = ["lasagna", "pizza", "lamb masala"]
friends_foods = my_foods[:]

my_foods.append("tortellini")
friends_foods.append("shepherd's pie")

print("My favourite foods are:")
for my_food in my_foods:
    print(my_food.title())

print("\nMy friend's favourite foods are:")
for friends_food in friends_foods:
    print(friends_food.title())

# 4-10
'''print("The first three items in the list are:")
print(my_foods[:3])

print("Three items in the middle of the list are:")
print(friend_foods[1:4])

print("The last three items in the list are:")
print(my_foods[-3:])'''

