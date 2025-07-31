import pickle

class Stack():
    contents = []

    def push(self, item):
        self.contents.append(item)

    def pop(self):
        if not self.contents:
            print("Stack underflow.")
            return

        return self.contents.pop()

    def top(self):
        if self.contents:
            return self.contents[-1]

def save():
    with open("stack.dat", "wb") as f:
        pickle.dump(test, f)

def load():
    with open("stack.dat", "rb") as f:
        obj = pickle.load(f)

    return obj

test = Stack()

while True:
    command = input(">>> ").lower().split()
    if command[0] == "push" and len(command) >= 2:
        test.push(command[1])

    elif command[0] == "pop":
        test.pop()

    elif command[0] == "top":
        print(test.top())

    elif command[0] == "print":
        print(", ".join(test.contents))

    elif command[0] == "save":
        save()

    elif command[0] == "load":
        test = load()

    elif command[0] == "exit":
        break
