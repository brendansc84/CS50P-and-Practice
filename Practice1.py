import math
def main():
    point1 = input("Point 1 - N,E,Z: ")
    point2 = input("Point 2 - N,E,Z: ")
    point1 = point1.split(",")
    point2 = point2.split(",")

    for p in point1:
        n1 = p[0]
        e1 = p[1]
        z1 = p[2]
    for p in point2:
        n2 = p[0]
        e2 = p[1]
        z2 = p[2]

    dn = n2 - n1
    de = e2 - e1
    dz = z2 - z1

    for p in point1:
        n1, e1, z1 = p[0], p[1], p[2]


main()