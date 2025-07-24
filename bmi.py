def bmi_category(w, h):
    if h <= 0:
        return "Height must be greater than zero."

    result = w / h ** 2
    bmi = round(result, 1)

    if bmi < 18.5:
        return f"{bmi} - Underweight"
    elif 18.5 <= result <= 24.9:
        return f"{bmi} - Normal"
    elif 25 <= result <= 29.9:
        return f"{bmi} - Overweight"
    else:
        return f"{bmi} - Obese"

print(bmi_category(95, 1.69))