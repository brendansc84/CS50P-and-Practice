people = [
    "Kirk Hammett",
    "Dimebag",
    "Robb Flynn",
    "Corey Taylor",
    "Courtney LaPlante"
                ]


people.insert(0, "Tatiana Shmayluk")
people.insert(3, "Laine Staley")
people.append("Jim Root")

k = people.pop(1)
d = people.pop(1)
l = people.pop(1)
r = people.pop(1)
c = people.pop(-1)
j = people.pop(1)
print(f"Sorry {k}, no more room! GTFO")
print(f"Sorry {d}, no more room! GTFO")
print(f"Sorry {l}, no more room! GTFO")
print(f"Sorry {r}, no more room! GTFO")
print(f"Sorry {c}, no more room! GTFO")
print(f"Sorry {j}, no more room! GTFO")

for p in people:
    print(p + ", you're more than welcome to still come over :)")