# Demonstrating line by line analysis of text file.

with open("README.md") as f:
    L = f.readlines()

n = 0

for line in L:
    if line[0] in "aeiouAEIOU":
        n += 1

print(f"There are {n} lines which start with a vowel.")
