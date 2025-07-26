def sum_odds(num):
    total = 0
    for n in num:
        if n % 2 != 0:
            total += n
    return total
print(sum_odds([1, 2, 3, 4, 5, 6]))