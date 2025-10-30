# Demonstrating the working of positional and keyword parameters.

# Create a function and call it using positional and keyword parameters.

def subtract(a, b):
    """
    Subtracts a from b.
    """
    result = b - a
    print(result)

subtract(1, 2)
subtract(2, 1)
subtract(a=1, b=2)
subtract(b=2, a=1)
subtract(1, b=2)
