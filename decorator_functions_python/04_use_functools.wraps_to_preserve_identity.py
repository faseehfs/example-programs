import functools

# After being decorated, functions report being the wrapper() inner
# function inside decorator. Although technically true, this isn’t
# very useful information.

# To fix this, decorators should use the @functools.wraps decorator,
# which will preserve information about the original function.

# NOTE: The @functools.wraps decorator uses functools.update_wrapper()
# to update special attributes like __name__ and __doc__ that are used
# in the introspection.

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs) # First call
        return func(*args, **kwargs) # Second call
    return wrapper_do_twice

@do_twice
def say_whee():
    print("Whee!")

print(say_whee.__name__)