#  Demonstrating working of default parameters.

def simpleInterest(P=1000, R=5, T=1):
    return P * R * T / 100

print(simpleInterest())
print(simpleInterest(2000))
print(simpleInterest(2000, 2))
print(simpleInterest(2000, 2, 2))