import random
def name_scrambler():
    name = input("Input Name: ")

    letters = list(name)
    random.shuffle(letters)
    scrambled = "".join(letters)

    print(scrambled)

name_scrambler()