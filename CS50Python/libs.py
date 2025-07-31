# Modules - library
# Importing modules; import math, import random, 
'''
from random import choice

coin = choice(["heads", "tails"])
print(coin)

import random

number = random.randint(1, 10)
print(number)

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
'''
'''
import statistics

print(statistics.mean([100, 90]))
'''
# command-line arguments
'''import sys
# sys.argv
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])
'''
import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv:
    print("hello, my name is", arg)