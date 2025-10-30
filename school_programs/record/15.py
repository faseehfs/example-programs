# Title: Demonstrating writing and reading data to and from a CSV file
# Aim: To write and read student names and marks from a CSV file using the csv module.

import csv

def writeCSV():
    with open("Stud.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Name", "Marks"])
        w.writerows([["Adisesh", 23], ["Crisvin", 18], ["Gautam", 14]])

def readCSV():
    with open("Stud.csv", "r", newline="") as f:
        for name, marks in csv.reader(f):
            print(name, marks)

writeCSV()
readCSV()
