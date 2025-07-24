"""
x = int(input("What's x?"))

if x % 2 == 0:
    print("even")
else:
    print("odd")
"""
""" **Boolean expression**
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
main()
"""

""" 'Pythonic' if_even def
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return True if n % 2 == 0 else False
main()
"""

# Simplified return boolean in is_even
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 ==0
main()