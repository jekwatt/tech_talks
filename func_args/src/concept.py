# Positional arguments (Arguments without default values)

def add_a(arg1, arg2):
    return arg1 + arg2


# Store result as a variable if you plan to reuse the return value later
result = add_a(1, 2)
print(result)

# Use the result of a function call only once
print(add_a(1, 2))


# Keyword arguments

# All positional arguments to Python functions can also be passed by keyword
def add_b(arg1, arg2):
    return arg1 + arg2


# Keyword Arguments can be placed in any order
print(add_b(arg2=3, arg1=4))


def add_c(arg1, arg2=10):
    return arg1 + arg2

# Explicitly provide 11 as the value, which overrides the default value of 10
print(add_c(5, 11))


# Keyword-only arguments; after splat (*) in the function signature

def add_d(arg1, *, kwarg1, kwarg2):
    return arg1 + kwarg1 + kwarg2


print(add_d(1, kwarg2=2, kwarg1=3))
print(f"add_d: {add_d(arg1=1, kwarg2=2, kwarg1=3)}")
print(f"add_d: {add_d(kwarg2=2, kwarg1=3, arg1=1)}")
# print(add_c(1, 2, 3))  # Output: TypeError


def add_e(arg1, *, kwarg1, kwarg2=20):  # set default value
    return arg1 + kwarg1 + kwarg2


print(add_e(1, kwarg1=3)) # with default value of kwarg2
print(f"add_e: {add_e(5, kwarg1=10, kwarg2=15)}")  # overwide default value of kwarg2
