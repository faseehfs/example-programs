# Demonstrating character by character analysis of text files.

with open("README.md", "r") as f:
    s = f.read()

u, l, v, c, d, sp = 0, 0, 0, 0, 0, 0

for char in s:
    if char.isalpha():
        if char.isupper():
            u += 1
        elif char.islower():
            l += 1
        if char in "aeiouAEIOU":
            v += 1
        else:
            c += 1
    elif char.isdigit():
        d += 1
    else:
        sp += 1

print(u, "upper case letters")
print(l, "lower case letters")
print(v, "vowels")
print(c, "consonants")
print(d, "digits")
print(sp, "special characters")
