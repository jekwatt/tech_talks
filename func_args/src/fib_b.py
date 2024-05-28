from functools import cache


# classic fibonacci examples


def fib_a(n):
    if n <= 1:
        return n
    return fib_a(n - 1) + fib_a(n - 2)


result_a = fib_a(10)
print(f"fib_a {result_a}")


@cache  # provide an empty memoization cache
def fib_b(n):
    if n <= 1:
        return n
    return fib_b(n - 1) + fib_b(n - 2)


result_b1 = fib_b(10)  # Providing the memo argument explicitly
print(f"Result {result_b1}")
