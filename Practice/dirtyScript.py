def mutual_turn_on(cara_horny, brendan_horny):
    sparks = 0

    for c, b in zip(cara_horny, brendan_horny):
        if c > 50 and b > 50:
            sparks += 1
            print("🔥 Mutual arousal detected — initiate face-sitting protocol 🔥")
        elif c > 50 or b > 50:
            print("⚡ One-sided horny — deploy teasing & cuddles")
        else:
            print("💤 No horny detected — deploy kindness and snacks")

    return f"Sparks this cycle: {sparks}"
    

# Today's vibes
cara_horny = [20, 55, 60, 40, 80]
brendan_horny = [75, 65, 45, 50, 90]

print(mutual_turn_on(cara_horny, brendan_horny))