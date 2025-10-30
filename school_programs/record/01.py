# Demonstrating the working of the random module and the randint() function.

# Write a Python program that simulates the throw of two dice using the random module.
# If both dice show the same number, you win; otherwise, you lose.

from random import randint

die1 = randint(1, 6)
die2 = randint(1, 6)

print(f"Die 1: {die1}, Die 2: {die2}")

if die1 == die2:
    print("You win!")
else:
    print("You lose.")
 