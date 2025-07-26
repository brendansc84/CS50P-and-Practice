def grade_report(students):
    report = {}

    for name, score in students:
        if 90 <= score <= 100:
            grade = "A"
        elif 80 <= score <= 89:
            grade = "B"
        elif 70 <= score <= 79:
            grade = "C"
        elif 60 <= score <= 69:
            grade = "D"
        else:
            grade = "F"

        report[name] = grade

    return report

print(grade_report([("Brendan", 85), ("Kellen", 92), ("Ryan", 10), ("Bill", 99), ("RC", 75)]))