# how to open and use csv file
# is an excel file
import csv

with open("data.csv")as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row[0],row[1],sep="! ")


