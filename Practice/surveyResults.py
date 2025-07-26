def tool_counter():
    responses = [
        {"name": "Brendan", "tools": ["Python", "TBC", "Civil3D"]},
        {"name": "Cara", "tools": ["TBC", "Civil3D"]},
        {"name": "Ayden", "tools": ["Python", "Trimble", "TBC"]},
        {"name": "Anthony", "tools": ["TBC", "Trimble"]}
    ]
    counts = {}

    for response in responses:
        for tool in response["tools"]:
            if tool in counts:
                counts[tool] += 1
            else:
                counts[tool] = 1

    return counts

print(tool_counter())