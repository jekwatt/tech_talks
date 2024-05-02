from utils import prefix_factory


# Use the decorator syntax

@prefix_factory("INFO")
def log_info(message):
    print(message)


@prefix_factory("ERROR")
def log_error(message):
    print(message)


@prefix_factory("DEBUG")
def log_debug(message):
    print(message)


# Define decorators using prefix_factory; to avoid TypeError: 'NoneType'
log_info = prefix_factory("INFO")
log_error = prefix_factory("ERROR")
log_debug = prefix_factory("DEBUG")


# Test the decorators
log_info("This is an information message")
log_error("This is an error message")
log_debug("This is a debug message")


# Test the decorators with additional keyword arguments
log_info("This is an information message", key1="value1", key2="value2")
log_error("This is an error message", key3="value3")
log_debug("This is an debug message", key2="value2", key3="value3")
