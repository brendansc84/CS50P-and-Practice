class Student:
    def __init__(self, name, house):     # instance method [method = function inside class] -- initializing an object -- self always 1st
        self.name = name                 # adding instance variable to object
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()