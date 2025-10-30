# Demonstrating line by line analysis of text file.

# Create a Python program which reads a text file line by line and prints the number of lines in it.

with open("README.md") as f:
    lines = 0
    while True:
        line = f.readline()
        if line == "":
            break
        lines += 1

print("Number of lines:", lines)
