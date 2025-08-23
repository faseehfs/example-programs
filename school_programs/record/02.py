def fruitful_greet(name: str):
    return(f"Hello {name}!")

def void_greet(name:str):
    print(f"Hello {name}!")

name = input("What is your name? ")

print(fruitful_greet(name))
void_greet(name)
