def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def say_whee(): # No arguments.
    print("Whee!")

say_whee()

@do_twice
def greet(name): # With arguments.
    print(f"Hello {name}!")

greet("World")