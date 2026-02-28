'''
def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_or_odd(16))'''

'''
def greet(name):
    return f"Hello, {name}!"
print(greet("Cara"))'''

def c_to_f(celsius):
    f = (celsius * 9/5) + 32
    return round(f, 1)
print(c_to_f(0))