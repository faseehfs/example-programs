# Demonstrating line by line analysis of text file.

with open("README.md") as f:
    L = f.readlines()

for line in L:
    if line[0] in "aeiouAEIOU":
        print(line, end='')
