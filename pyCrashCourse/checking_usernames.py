current_users = ['syora', 'rhazjin', 'alythea', 'vixzle', 'valysan']

new_users = ['Moozen', 'SyoRa', 'Iladria', 'VIXZLE', 'Elorath']

if new_users:
    for new in new_users:
        if new.lower() in current_users:    #   .lower() needs to attach to created item; not in the line that creates it
            print("Username unavailable")
        else:
            print(f"Welcome, {new}")
else:
    print("Please enter desired username.")