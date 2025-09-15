cities = {
    'calgary': {
        'location': 'alberta, canada',
        'population': '1.5 million',
        'fact': 'calgary was home to the 1988 winter olympics'
    },
    'oslo': {
        'location': 'norway',
        'population': '1.1 million',
        'fact': 'vikings - that is all.'
    },
    'cancun': {
        'location': 'mexico',
        'population': '0.9 million',
        'fact': 'cancun is a party city'
    }
}

for city, facts in cities.items():
    print(f"\nCity: {city.title()}")
    location = facts['location']
    population = facts['population']
    fact = facts['fact']

    print(f"Location: {location.title()}")
    print(f"Population: {population}")
    print(f"City Fact: {fact.capitalize()}")