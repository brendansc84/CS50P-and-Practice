import random
def name_scrambler():
    name = input("Input Name: ")

    while True:
        letters = list(name)
        random.shuffle(letters)
        scrambled = "".join(letters)
        print(scrambled.title())
    
        response = input("Press Enter to scramble again, or type 'quit' to stop: ").lower()
        if response == "quit":
            break

name_scrambler()