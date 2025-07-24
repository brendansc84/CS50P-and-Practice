"""def main():
    print_column(3)

def print_column(height):
    print("#\n" * height, end="")"""


"""def main():
    print_row(4)

def print_row(width):
    print("?" * width)"""

def main():
    print_square(3)

"""def print_square(size):
     # for each row in square
    for i in range(size):
        # for each brick in row
        for j in range(size):
            # print brick
            print("#", end="")
        # Why bro
        print()"""

"""def print_square(size):
    for i in range(size):
        print("#" * size)"""

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()