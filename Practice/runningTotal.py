def running_total(nums):
    total = 0
    li = []
    
    for n in nums:
        total += n
        li.append(total)
    return li

print(running_total([1, 2, 3, 4]))