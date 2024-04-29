from utils import reverse_factory


# Use the decorator syntax

@reverse_factory
def hi(text):
    print(f"Hi decorator, {text}")


@reverse_factory
def hello(text):
    print(f"Hello decorator, {text}")


@reverse_factory
def bye(text):
    print(f"Bye decorator, {text}")


hi("Decorator")
hello("Decorator")
bye("Decorator")


# functools.wraps(func) is used to preserve the metadata of the original function
# The original underlying function is accessible through the __wrapped__ attribute
undecorated_hi = hi.__wrapped__

# Now you can call the undecorated function
undecorated_hi("Decorator")
