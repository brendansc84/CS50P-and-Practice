import random


def main():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
        except ValueError:
            continue

    rand = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0 or guess > level:
                continue
            elif rand > guess:
                print("Too small!")
            elif rand < guess:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError:
            continue
main()