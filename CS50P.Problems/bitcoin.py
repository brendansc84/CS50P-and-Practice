import requests
import sys

# site & key (rest.coincap.io/v3/assets/bitcoin?apiKey=28e38c86ba71a8f80b98c1361fcf05c32722df3afcd84fa3b1e75520090e2060)

def main():
    if len(sys.argv)!= 2:
        sys.exit("Missing command-line argument")

    try:
        count = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=28e38c86ba71a8f80b98c1361fcf05c32722df3afcd84fa3b1e75520090e2060"
            )
        response.raise_for_status()
        content = response.json()
        price = float(content["data"]["priceUsd"])
        btc = count * price
        print(f"${btc:,.4f}")
    except requests.HTTPError:
        print("Couldn't complete request.")
        return

main()