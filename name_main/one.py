#!/usr/bin/env python3

"""one.py
Testing if the module is being run directly or being used as an import"""


print(">>>Top level in one.py")

print(repr(__name__))


def main():
    func()


def func():
    print("hello from one.py")


# LOTS MORE FUNCTIONS


if __name__ == '__main__':
    print("one.py is being run directly")
    main()
else:
    print("one.py is being run in another module")
