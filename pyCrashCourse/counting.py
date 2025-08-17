# 4-3, 4-4 counts
'''
for n in range(1, 1000001):
    print(n)
'''
# 4-5 min, max, sum
'''
li = range(1, 1000001)
print(f"Min: {min(li)}")
print(f"Max: {max(li)}")
print(f"Sum: {sum(li)}")
'''
# 4-6 Odds
'''
li = range(1, 11)
for n in li:
    if n % 2 != 0:
        print(n)
'''
# 4-7
'''
li = range(1, 31)
for n in li:
    if n % 3 == 0:
        print(n)
'''
# 4-8 Cubes
'''
li = range(1, 11)
for n in li:
    x = n**3
    print(x)
'''
# 4-9 Cube list comp
cubes = [n**3 for n in range(1, 11)]
print(cubes)

# FUCKING NAILED IT!!!! Only ish, couldn't get cube comp to print vertical, but hella minor.