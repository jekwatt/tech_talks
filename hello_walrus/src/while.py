num_list = [1, 2, 3, 4, 5]


# With while loop
while True:
    n = len(num_list)
    if n > 0:
        print(num_list.pop())
    else:
        break


# With walrus operator
while (n := len(num_list)) > 0:
    print(num_list.pop())


# Without modifying the list
while num_list:
    print(num_list[-1])
    num_list = num_list[:-1]
