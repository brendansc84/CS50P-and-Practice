def main():
    d = 50

    while d > 0:
        print(f"Amount Due: {d}")
        i = int(input("Insert Coin: "))
        
        if i in [25, 10, 5]:
            d -= i
        else:
            print("Invalid Coin")

    print(f"Change Owed: {abs(d)}")

main()