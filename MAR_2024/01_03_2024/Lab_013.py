# writing data in csv files
import csv

test_data = [
    ['Name', 'Age', 'City'],
    ['Alina', '34', 'London'],
    ['John', '25', 'New York']
]

with open("mydata.csv", 'w')as file:
    writer = csv.writer(file)
    for data in test_data:
        writer.writerow(data)

print("Close file")