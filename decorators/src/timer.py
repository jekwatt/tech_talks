from functools import cache, lru_cache

from utils import timer


# It's expected to see varying execution times without caching mechanisms like 'cache' or 'lru_cache'.
# Without caching, each recursive call to the fib recalculates the values from scratch,
# leading to fluctuations in execution times.

@timer
def fib_a(n):
    if n <= 1:
        return n
    return fib_a(n-1) + fib_a(n-2)

result_a = fib_a(10)
print(f"fib_a {result_a}")


# You can stack multiple decorators

# It caches all intermediate results during the recursive calls,
# leading to faster execution times in subsequent call.

@cache
@timer
def fib_b(n):
    if n <= 1:
        return n
    return fib_b(n-1) + fib_b(n-2)

result_b = fib_b(10)
print(f"fib_b {result_b}")


# Only the most recently used results are cached, up to a maximum of 128 unique arguments.
# As a result, you may observe slightly longer execution times in subsequent calls compared to cache.

@lru_cache(maxsize=128)
@timer
def fib_c(n):
    if n <= 1:
        return n
    return fib_c(n-1) + fib_c(n-2)

result_c = fib_c(10)
print(f"fib_c {result_c}")
