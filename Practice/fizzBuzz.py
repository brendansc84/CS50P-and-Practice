def fizzbuzz_lite(num):
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
print(fizzbuzz_lite(15))