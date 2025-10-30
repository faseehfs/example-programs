# Demonstrating the working of fruitful and void functions

# Define two Python functions that perform the same task:
# one returns a value, while the other prints the value directly.

def fruitful_greet(name: str):
    return f"Hello {name}!"

def void_greet(name: str):
    print(f"Hello {name}!")

print(fruitful_greet("John"))
void_greet("John")
