# Demonstrating working of default parameters.

# Create a function which takes some default arguments and call it with and without arguments.

def simple_interest(P=1000, R=5, T=1):
    return P * R * T / 100

print(simple_interest())
print(simple_interest(2000))
print(simple_interest(2000, 2))
print(simple_interest(2000, 2, 2))
   