# Title: Demonstrating simple operations on a stack
# Aim: To implement basic stack operations (push, pop, display) using a list.

stack = []

def push(val):
    stack.append(val)

def pop():
    if stack:
        print("Popped:", stack.pop())
    else:
        print("Stack Underflow")

def display():
    print("Stack:", stack if stack else "Empty")

push(4)
push(9)
push(3)
display()
pop()
display()
push(-5)
display()
pop()
display()
