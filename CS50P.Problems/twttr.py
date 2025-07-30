def main():
    tweet = input("Input: ")
    print("Output: ", shorten(tweet))

def shorten(word):
    result = ""
    for n in word:
        if n.lower() not in "aeiou":
            result += n
    return result

if __name__ == "__main__":
    main()