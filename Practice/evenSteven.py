def even_numbers(nums):
    li = []

    for n in nums:
        if n % 2 == 0:
            li.append(n)
    return li

print(even_numbers([1, 2, 3, 4, 5, 6]))