# Demonstrating character by character analysis of text files.

# Create a function which counts the number of uppercase letters and lowercase letters in a text file.

with open("README.md", "r") as f:
    s = f.read()

u, l = 0, 0,

for char in s:
    if char.isupper():
        u += 1
    elif char.islower():
        l += 1

print(u, "upper case letters")
print(l, "lower case letters")