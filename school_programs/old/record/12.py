# Demonstrating writing, reading and appending lists to and from a binary file.

import pickle

def writeBin():
    with open("Nations1.bin", 'wb') as out:
        pickle.dump(["India", "New Delhi"], out)
        pickle.dump(["Pakistan", "Islamabad"], out)
        pickle.dump(["China", "Beijing"], out)

def readBin():
    with open("Nations1.bin", 'rb') as inn:
        try:
            while True:
                obj = pickle.load(inn)
                print(obj)
        except EOFError:
            pass

def addBin():
    with open("Nations1.bin", 'ab') as out:
        pickle.dump(["Nepal", "Kathmandu"], out)

writeBin()
readBin()
print()
addBin()
readBin()
