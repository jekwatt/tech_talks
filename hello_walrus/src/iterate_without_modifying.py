num_list = [1, 3, 4, 5, 2]


def iterate_without_modifying_list(num_list):
    num_list.sort()
    while num_list:
        print(num_list[-1])
        num_list = num_list[:-1]  # making a new copy


# Example usage

print("\nOriginal num_list:", num_list)

# Call the function with a copy of num_list
iterate_without_modifying_list(num_list[:])
print("\nAfter calling iterate_without_modifying_list with a copy:", num_list)

# Call the function second time with the original num_list
iterate_without_modifying_list(num_list)
print("\nAfter calling iterate_without_modifying_list with the original:", num_list)

# Call the function third time with the original num_list
iterate_without_modifying_list(num_list)
print("\nAfter calling iterate_without_modifying_list with the original again:", num_list)
