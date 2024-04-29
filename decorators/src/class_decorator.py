from utils import MyDecorator


# class as a decorator

class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Decorator is called")
        return self.func(*args, **kwargs)


# Usage

@MyDecorator
def greet(name):
    print(f"Hello, {name}!")


greet("Jennifer")
