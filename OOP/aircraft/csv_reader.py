import csv

with open(
        'h:\\personal\\Explore-language\\Python\\OOP\\aircraft\\data\\data.csv',
        'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(sorted(row))
