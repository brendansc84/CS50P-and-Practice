def boombang(num):
    li = []
    for n in range(1, num + 1):
        if n % 4 == 0 and n % 6 == 0:
            li.append("BoomBang")
        elif n % 4 == 0:
            li.append("Boom")
        elif n % 6 == 0:
            li.append("Bang")
        else:
            li.append(n)
    return li
print(boombang(12))