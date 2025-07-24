x = int(input("What's x? "))
y = int(input("What's y? "))

"""
Original question:
 if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")
"""

"""
# Less calculations instead of running all 3 regardless
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
# another instance of 'elif' asks another question rather than deciding false is ==
else x == y:
    print("x is equal to y")
"""

# if x != y -- Not equal to
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# Could my code be better; could it be simplified or tightened up?

