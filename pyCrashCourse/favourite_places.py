favourite_places = {
    'colin': [
        'germany',
        'scotland',
        'turkiye'
        ],
    'cara': [
        'scotland',
        'ireland',
        'bora-bora'
        ],
    'brendan': [
        'norway',
        'mexico',
        'bora-bora'
        ],
    }

for name, places in favourite_places.items():
    formatted_places = ", ".join(place.title() for place in places)
    print(f"Name: {name.title()}")
    print(f"Favourite Places: {formatted_places}\n")
