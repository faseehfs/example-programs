# Title: Demonstrating write, read & append operations on a dictionary using a binary file
# Aim: To store, read, and update a dictionary of numbers in a binary file using pickle and 'rb+' mode.

import pickle

def writeBin():
    with open("data.bin", "wb") as f:
        pickle.dump({"one": 1, "two": 2, "three": 3}, f)

def readBin():
    with open("data.bin", "rb") as f:
        print(pickle.load(f))

def addBin():
    with open("data.bin", "rb+") as f:
        d = pickle.load(f)
        d["four"] = 4
        f.seek(0)
        pickle.dump(d, f)

writeBin()
readBin()
addBin()
readBin()
