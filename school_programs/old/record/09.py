# Demonstrating line by line analysis of text file.

with open("README.md") as f:
    c = 0
    while True:
        line = f.readline()
        if line == "":
            break
        c += 1

print("Number of lines:", c)
