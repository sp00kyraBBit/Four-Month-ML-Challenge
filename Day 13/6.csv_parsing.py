import csv

with open("read.csv","r",encoding="utf-8") as f:
    data = csv.DictReader(f)
    for row in data:
        print(row)  # each row is a dictionary
