import random

while True:
    try:
        length = int(input("Password length: "))
    except:
        print("Invalid.")
    else:
        break

password = ""

for i in range(length):
    password += chr(random.randint(97, 122))

print("Password:", password)
