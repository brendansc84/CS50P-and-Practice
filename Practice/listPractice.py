'''
def main():
    foods = ["Lasagna", "Blackened Chicken", "Burgers", "Pizza", "Poutine"]
    for f in foods:
        if f == foods[2]:
            print("🍕")
        else:
            print(f.upper())
main()
'''

def main():
    foods = ["Lasagna", "Blackened Chicken", "Burgers", "Pizza", "Poutine"]
    for f in foods:
        print(f.upper())
    foods[2] = "🍕"
    print(foods)
main()