# Defining the decorator function

def my_decorator(func):
    def wrapper(*args, **kwargs):
        # return func(*args, *kwargs)
        value = func(*args, *kwargs)
        return value
    return wrapper


# Defining the original functions

def hello():
    print("Inside original hello function")
    print(f"Hello")


# Applying the decorator manually

my_decorator(hello)()


# Function aliasing with decorator

# Apply the decorator to hello function
hello = my_decorator(hello)
# Call the decorated hello function
hello()


# Using the decorator syntax (@)

@my_decorator
def hello():
    print("Inside decorated hello function")
    print(f"Bye")

hello()
