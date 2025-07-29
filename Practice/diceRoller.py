import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    return f"{die1} + {die2} = {total}"

for i in range(10):
    print(f"Roll {i+1}: {roll_dice()}")