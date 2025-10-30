# Title: Demonstrating writing, reading, and calculating average from a CSV file
# Aim: To store student marks in a CSV file and display the overall average using the csv module.

import csv

def writeCSV():
    with open("Marks.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Name", "Marks"])
        w.writerows([["K. Mathews", 60], ["A. George", 70], ["N. Thomas", 65]])

def readCSV():
    with open("Marks.csv", "r", newline="") as f:
        rows = list(csv.reader(f))[1:]
        total = 0
        for name, marks in rows:
            print(name, marks)
            total += int(marks)
        print("Overall Average:", total // len(rows))

writeCSV()
readCSV()
 