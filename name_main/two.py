#! /usr/bin/env python3

"""two.py
Second module for testing"""

import one


print(">>>Top level in two.py")

print(repr(__name__))
print(repr(__name__))


one.main()

one.func()


def main():
    print("hello from two.py")


if __name__ == '__main__':
    print("two.py is being run directly")
    main()
else:
    print("two.py is being imported into another module")
