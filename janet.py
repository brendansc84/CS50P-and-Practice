# Grades
'''def main():
    text = input("Percentage: ")

    try:
        text = int(text)
        if 90 <= text <= 100:
            print("A")
        elif 80 <= text <= 89:
            print("B")
        elif 70 <= text <= 79:
            print("C")
        elif 60 <= text <= 69:
            print("D")
        elif 0 <= text <= 60:
            print("F")
        else:
            print("Please enter a number between 0-100")
    except ValueError:
        print("Please enter a number between 0-100")

main()'''

# Vowel Out
'''def main():
    text = input("Enter text: ")
    vowels = ("aeiouAEIOU")
    result = ""

    for char in text:
        if char not in vowels:
            result += char
    print(result)
main()'''

# Capitalize the Title
'''def main(): # defining the main function
    text = input("Enter text: ") # user input
    word = text.split() # split text into a list of words, using spaces as the default separator
    modified_words = [] # create an empty list to store the modified words

    for w in word: # loop through each word in the list - w represents each individual word
        if len(w) >= 4: # if the length of w is equal to or greater than 4...
            modified_words.append(w.title()) # ...add the word to the list with its first letter capitalized
        else: # if w is NOT equal to or greater than 4...
            modified_words.append(w) # ...Take the null factor of 'modified_words', add w as it is.
    final = " ".join(modified_words) # join the list of modified_words into a single string, separated by spaces
    
    print(final) # self explanatory; print 'final', the joined result of null + modified_words

main() # execute main()'''

# Filter long Words Opt 1
'''def filter_long_words(words, n):
    mod = []
    for w in words:
        if len(w) > n:
            mod.append(w)
    return mod

print(filter_long_words(["apple", "banana", "kiwi", "mango"], 4))

# Filter long Words Opt 2
def filter_long_words():
    text = input("Enter words: ")
    words = text.split()
    n = int(input("Enter minimum word length: "))
    
    mod = []
    for w in words:
        if len(w) > n:
            mod.append(w)

    print(mod)

filter_long_words()'''

# Vowel Remover
'''def remove_vowels(text):
    l = ("aeiouAEIOU")
    result = ""

    for v in text:
        if v not in l:
            result += v
    return result

print(remove_vowels("Test string to remove vowels from this input"))'''

# Word Counter
'''def count_words(text):
    a = text.split()

    return len(a)

print(count_words("The quick brown fox jumps over the lazy dog"))'''

# Shortest Word
'''def shortest_word(text): # define the function
    words = text.split() # create a list of the words in 'text'
    shortest = words[0]
    
    for w in words:
        if len(w) < len(shortest):
            shortest = w
    return shortest

print(shortest_word("Python is a glorious and magnificent language"))'''

# Letter Counter
'''def letter_counter(text, letter):
    count = 0
    for char in text:
        if char.lower() == letter.lower():
            count += 1
    return count
print(letter_counter("Whatever text you want", "t"))'''

# Tip Calculator
'''def calculate_tip(bill, tip_percent):
    tip_percent = tip_percent / 100
    tip = bill * tip_percent
    return tip + bill
print(f"${calculate_tip(120, 20):.2f}")'''

# Score Analyzer
'''def score_analyzer(scores):
    num = scores.split(",")
    passing_scores = []
    
    for n in num:
        n_int = int(n)
        if n_int >= 70:
            passing_scores.append(n_int)

    if len(passing_scores) == 0:
        return 0
    
    average = sum(passing_scores) / len(passing_scores)
    return round(average, 2)

print(score_analyzer("88,72,91,65"))'''

# Letter Grade Filter
'''def grade_filter(grade):
    num = grade.split(",")
    passing = []

    for n in num:
        n_int = int(n)
        if n_int >= 60:
            passing.append(n_int)

    grades = []

    for score in passing:
        if 90 <= score <= 100:
            grades.append("A")
        elif 80 <= score <= 89:
            grades.append("B")
        elif 70 <= score <= 79:
            grades.append("C")
        elif 60 <= score <= 69:
            grades.append("D")
    return grades

print(grade_filter("95,67,88,74,59"))'''

# Moving onto bigger things
# Hopefully this has all been retained, but I'll do some light warmups before we dive back in; as of July 23, 2025 I now have 'Python from Scratch', along with CS50P + Janet (ChatGPT). Onward and upward.

# Even Stevens - July 23 Warmup - "Write a function that takes a string of numbers separated by commas (e.g., "12,7,4,9,16,3") and returns a list of the even numbers, but squared."

'''def even_stevens(numbers):
    num = numbers.split(",")
    even = []

    for n in num:
        i = int(n)
        if i % 2 == 0:
            even.append(i ** 2)
    
    return sorted(even, reverse=True)

print(even_stevens("12,7,4,9,16,3"))'''

# Pro Version:    (Def not there yet, but good reference)
'''def even_stevens(numbers):
    return sorted([int(n)**2 for n in numbers.split(",") if int(n) % 2 == 0], reverse=True)
print(even_stevens("12,7,4,9,16,3"))'''

# BMI Function
'''def bmi(w, h):
    result = w / h ** 2
    return round(result, 1)

print(bmi(75, 1.8))'''

# quick problem
'''def magic_number():
    x = 7
    return x * 11

x = 3
print(magic_number())
print(x)'''

# Quick problem
'''def bmi(w, h=1.75):
    result = w / h ** 2
    return round(result, 1)
print(bmi(95, 1.69))
print(bmi(95))'''

# BMI Categorization
'''def bmi_category(w, h):
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

print(bmi_category(95, 1.69))'''

# Loops
'''
for i in range(5):  # we know we want 5 times; i will repeat for range(x)
    print(i)
'''
'''
x = 0
while x < 5:
    print(x)
    x += 1
'''
'''
for i in range(10):
    if i == 6:
        break  # stop the loop completely
    if i % 2 == 0:
        continue  # skip the rest of the loop and go to the next
    print(i)
'''

# Even Counter
'''
def even_counter(numbers):
    num = numbers.split(",")
    even = []

    for n in num:
        n = int(n)
        if n % 2 == 0:
            even.append(n)
        
    return len(even)

print(even_counter("5,6,7,8,10,11"))
'''
# no-list version - lower memory usage
'''
def even_counter(numbers):
    count = 0
    for n in numbers.split(","):
        if int(n) % 2 == 0:
            count += 1
    return count
print(even_counter("5,6,7,8,10,11,13,16,21,23,28"))
'''
# even counter while loop
'''
def even_counter(numbers):
    num_list = numbers.split(",")
    index = 0
    count = 0

    while index < len(num_list):
        n = int(num_list[index])
        if n % 2 == 0:
            count += 1
        index += 1

    return count

print(even_counter("5,6,7,8,10,11"))
'''

text = "FLIGHT"
for i, ch in enumerate(text, 1):
    print(ch, i)