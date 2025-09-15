rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'bow': 'calgary',
    'colorado': 'the grand canyon',
    'oldman': 'lethbridge'
}

for river, place in rivers.items():
    print(f"The {river.title()} river runs through {place.title()}.")