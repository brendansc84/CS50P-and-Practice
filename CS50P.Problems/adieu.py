import inflect


def main():
    li = []

    try:
        while True:
            name = input("Name: ")
            li.append(name)
    except EOFError:
        pass

    p = inflect.engine()
    names = p.join(li)

    print("Adieu, adieu, to " + names)
main()