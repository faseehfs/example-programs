# Create a binary file with name and roll number.
# Search for a given roll number and display the name, if not found display appropriate message. 

import pickle

def create():
    data = []
    while True:
        name = input("Name: ")
        if name:
            data.append(name)
        else:
            print("\033[F\033[K", end='')
            break
        
    with open("data.dat", "wb") as f:
        pickle.dump(data, f)

def search():
    roll = int(input("Roll no: "))

    with open("data.dat", "rb") as f:
        data = pickle.load(f)
    
    if roll <= len(data) and roll > 0:
        print(data[roll - 1])
    else:
        print(f"Roll number {roll} is invalid.")

create()
search()
