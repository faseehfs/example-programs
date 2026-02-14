class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


my_stack = Stack()

my_stack.push("A")
my_stack.push("B")
my_stack.push("C")

print("Stack: ", my_stack.stack)
print("Pop: ", my_stack.pop())
print("Stack after Pop: ", my_stack.stack)
print("Peek: ", my_stack.peek())
print("isEmpty: ", my_stack.is_empty())
print("Size: ", my_stack.size())
