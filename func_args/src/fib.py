# classic fibonacci examples


def fib_a(n):
    if n <= 1:
        return n
    return fib_a(n - 1) + fib_a(n - 2)


result_a = fib_a(10)
print(f"fib_a {result_a}")


# splat(*) followed by keyword-only args


def fib_b(n, *, memo={}):  # provide an empty memoization cache
    if n <= 1:
        return n
    elif n not in memo:
        memo[n] = fib_b(n - 1, memo=memo) + fib_b(n - 2, memo=memo)
    return memo[n]


result_b1 = fib_b(10, memo={})  # Providing the memo argument explicitly
print(f"Result {result_b1}")

# Starting a new Fibonacci sequence with an empty memoization cache
result_b2 = fib_b(10, memo={})
print(result_b2)
