import pickle

HELP = """
push element : push an element into the stack
pop element  : delete an element from the stack and show it
top          : shows the topmost element
print        : shows the whole stack
save         : saves the stack in "stack.dat"
load         : loads the stack from "stack.dat"
exit         : exits the program
"""

class Stack():
    contents = []

    def push(self, item):
        self.contents.append(item)

    def pop(self):
        if not self.contents:
            return "Stack underflow."

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
    if command[0] == "help":
        print(HELP)

    elif command[0] == "push" and len(command) >= 2:
        test.push(command[1])

    elif command[0] == "pop":
        print(test.pop())

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

    else:
        print(f'Command "{command[0]}" is not found.')
