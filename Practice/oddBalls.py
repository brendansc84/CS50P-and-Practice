def filter_oddballs(numbers):
    nums = numbers.split(",")
    li = []

    for n in nums:
        i = int(n)
        if i % 2 != 0:
            li.append(i)
    return sorted(li, reverse=True)

print(filter_oddballs("12,7,5,10,3,4,9"))