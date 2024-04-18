num_list = [1, 2, 3, 4, 5]


def iterate_with_while_loop(num_list):
    while True:
        n = len(num_list)
        if n > 0:
            print(num_list.pop())
        else:
            break


def iterate_with_walrus_operator(num_list):
    while (n := len(num_list)) > 0:
        print(num_list.pop())


# Example usage

print("Iterating with while loop:")
# Passing a copy of the original list to avoid modification
iterate_with_while_loop(num_list[:])

print("\nIterating with walrus operator:")
iterate_with_walrus_operator(num_list[:])
