# A simple decorator.

def my_decorator(func):
    def wrapper():
        print("Something before the function.")
        func()
        print("Something after the function.")
    return wrapper

@my_decorator # Calling the decorator.
# The function that immediately follows @my_decorator is passed as the argument to the decorator.
def say_hello():
    print("Hello!")

say_hello()
