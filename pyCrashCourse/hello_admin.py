usernames = ['Syora', 'Rhazjin', 'Alythea', 'Admin', 'Vixzle']


if usernames:
    for name in usernames:
        if name == 'Admin':
            print(f"Hello, Supreme Leader {name}. Would you like a status report?")
        else:
            print(f"Welome, {name}!")
else:
    print("Well shit. We need some users...")