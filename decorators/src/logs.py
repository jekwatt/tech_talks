from utils import log


@log
def add(x, y):
    return x + y

@log
def multiply(x, y):
    return x * y


# Test the decorated functions

print(f"Result: {add(3, 5)}")
print(f"Result: {multiply(4, 6)}")

print(f"Result: {add(3, y=10)}")
print(f"Result: {multiply(x=5, y=6)}")
