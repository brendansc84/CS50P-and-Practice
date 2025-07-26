def passing_students():
    students = [
        {"name": "Brendan", "grade": 58},
        {"name": "Cara", "grade": 51},
        {"name": "McKenzie", "grade": 86},
        {"name": "Ayden", "grade": 99},
        {"name": "Brody", "grade": 95},
        {"name": "Anthony", "grade": 20}
    ]
    passing = []

    for student in students:
        if student["grade"] >= 60:
            passing.append(student["name"])

    return passing
print(passing_students())