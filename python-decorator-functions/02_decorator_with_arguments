def my_decorator(arg):
    def decorator(func):
        def wrapper():
            print(f"The argument passed to the decorator: {arg}")
            func()
            print("Something after the function.")
        return wrapper
    return decorator

@my_decorator("abcd")
def say_hello():
    print("Hello!")

say_hello()


# my_decorator gets the argument from the statement:
#       @my_decorator("abcd")

# decorator in my_decorator also needs an argument. Since it takes a
# function as an argument, it would be the function immediately below
# the decorator calling statement. In this case, say_hello.
