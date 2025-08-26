# Read a text file line by line and display each word separated by a #.

with open("README.md", "r") as f:
    line = f.readline()
    while line != "":
        print("#".join(line.split()))
        line = f.readline()
