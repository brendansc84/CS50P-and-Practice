"""
i = 0
while i < 3:
    print("meow")
    i += 1
"""

""" [] brackets = list
for i in [0, 1, 2]:
    print("meow")
"""
"""
for i in range(3):
    print("meow")
"""
"""
for _ in range(3):
    print("meow")
"""

""" super simple "Pythonic"
print("meow\n" * 3, end="")
"""

""" user input
while True:
    n = int(input("What's n? "))
    if n > 0:
        break
for _ in range(n):
    print("meow")
"""

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")
