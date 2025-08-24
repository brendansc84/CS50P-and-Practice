from tabulate import tabulate
import csv

with open("sicilian.csv") as file:
    print(tabulate((csv.DictReader(file)), headers="keys", tablefmt="outline"))