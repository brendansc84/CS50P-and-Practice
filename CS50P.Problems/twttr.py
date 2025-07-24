def main():
    tweet = input("Input: ")
    print("Output: ", short(tweet))

def short(text):
    result = ""
    for n in text:
        if n.lower() not in "aeiou":
            result += n
    return result

main()