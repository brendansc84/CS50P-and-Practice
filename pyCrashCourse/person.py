cara = {
    'first name': 'cara',
    'last name': 'gillespie',
    'age': 35,
    'city': 'calgary'
    }


mckenzie = {
    'first name': 'mckenzie',
    'last name': 'ostafie',
    'age': 17,
    'city': 'calgary'
    }

brody = {
    'first name': 'brody',
    'last name': 'cormier',
    'age': 13,
    'city': 'lethbridge'
    }

people = [cara, mckenzie, brody]

for person in people:
    print(f"First name: {person['first name'].title()}")
    print(f"Last name: {person['last name'].title()}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city'].title()}\n")