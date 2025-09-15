moose = {
    'name': 'moose',
    'animal': 'dog',
    'owner': 'cara'
    }
whiskers = {
    'name': 'whiskers',
    'animal': 'cat',
    'owner': 'lynne'
    }
spike = {
    'name': 'spike',
    'animal': 'guinea pig',
    'owner': 'brendan'
    }

pets = [moose, whiskers, spike]

for pet in pets:
    print(f"Name:    {pet['name'].title()}")
    print(f"Animal:  {pet['animal'].title()}")
    print(f"Owner:   {pet['owner'].title()}\n")
    