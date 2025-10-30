# Demonstrating write, read & appending dictionary to and from a binary file using 'rb' and 'wb' modes.

# Create functions to read and write objects to a binary file. Use them to insert a dictionary, read it, and append an element to it using Python file handling.

import pickle
FILE = "file.bin"

def write(obj):
    with open(FILE, "wb") as f:
        pickle.dump(obj, f)
    
def read():
    with open(FILE, "rb") as f:
        return pickle.load(f)

write({"one": 1, "two": 2})
dict = read()
print(dict)
dict.update({"three": 3})
write(dict)
print(read())
