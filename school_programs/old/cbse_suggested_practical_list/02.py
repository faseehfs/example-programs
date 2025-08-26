# Read a text file and display the number of vowels/consonants/uppercase/lowercase characters in the file.

with open("README.md", "r") as f:
    text = f.read()

VOWELS = "aeiou"
v, c = 0, 0

for char in text:
    if char.lower() in VOWELS:
        v += 1
    else:
        if char.isalpha():
            c += 1

u, l = 0, 0

for char in text:
    if char.islower():
        l += 1
    elif char.isupper():
        u += 1

print(v, c, u, l)
