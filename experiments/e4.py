import csv

with open("../weather.csv") as file:
    # csv.reader(file) will give us Iterator, it is not readable, so we need to convert it into List
    data = list(csv.reader(file))

city = input("Enter a city: ")

for row in data[1:]:
    if row[0] == city:
        print(row[1])