# Demonstrating writing, reading and appending lists to and from a binary file.

import pickle

def writeBin():
    with open("numbers.bin", 'wb') as f:
        pickle.dump(["one", 1], f)
        pickle.dump(["two", 2], f)

def readBin():
    with open("numbers.bin", 'rb') as f:
        try:
            while True:
                obj = pickle.load(f)
                print(obj)
        except EOFError:
            pass
 
def addThreeBin():
    with open("numbers.bin", 'ab') as f:
        pickle.dump(["three", 3], f)

writeBin()
readBin()
print()
addThreeBin()
readBin()
