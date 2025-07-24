def main():
    everything = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    everything = everything.strip().lower()
    
    if everything in ["42", "forty-two", "forty two"]:
        print("Yes")
    else:
        print("No")

main()