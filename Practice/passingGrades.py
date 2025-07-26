def passing_grades(grades):
    nums = []

    for g in grades:
        if g > 60:
            nums.append(g)

    return nums
print(passing_grades([72, 55, 89, 40, 67, 91, 59]))