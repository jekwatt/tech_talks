import functools
import time
import datetime


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper


# Although prefix_factory itself is not a decorator,
# it can be used to create decorator-like behavior.

def prefix_factory(prefix):
    # It only takes a single argument (text)
    def prefix_printer(text):
        print(f"{prefix}: {text}")
    return prefix_printer


# Better
def prefix_factory(prefix):
    # More versatile
    # It can handle any number of positional and keyword arguments
    def prefix_printer(*args, **kwargs):
        print(f"{prefix}: {args}, {kwargs}")
    return prefix_printer


# Reverse print function
def tnirp(text):
    print(text[::])


def reverse_factory(func):
    @functools.wraps(func)  # Preserve the original function's metadata
    def reverse_caller(text):
        func(text[::-1])
    return reverse_caller


def log(func):  # log is not reserved word
    def wrapper(*args, **kwargs):
        with open("logs.txt", "a") as f:  # Will create "logs.txt" file and append
            # repr ensures that their original types and values are preserved
            arg_str = ', '.join([repr(arg) for arg in args])
            # {value!r} to use its __repr__ method
            kwarg_str = ', '.join([f"{key}={value!r}" for key, value in kwargs.items()])
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_message = f"Called {func.__name__} with args: {arg_str}, kwargs: {kwarg_str} at {timestamp}\n"
            f.write(log_message)
        return func(*args, **kwargs)
    return wrapper
