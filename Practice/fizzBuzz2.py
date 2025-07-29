def fizzbuzz(num):
    li = []
    for n in range(1, num + 1):
        if n % 3 == 0 and n % 5 == 0:
            li.append("FizzBuzz")
        elif n % 3 == 0:
            li.append("Fizz")
        elif n % 5 == 0:
            li.append("Buzz")
        else:
            li.append(n)
    return li
# print(fizzbuzz(50)) - regular
print("\n".join(str(i) for i in fizzbuzz(50))) # One result per line