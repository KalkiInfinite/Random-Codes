def find_divisible_tuples(test_list, divisor):
    return [tup for tup in test_list if all(x % divisor == 0 for x in tup)]

test_list = [(2, 4, 6), (3, 6, 9), (5, 10, 15), (7, 14, 21)]
divisor = 3
divisible_tuples = find_divisible_tuples(test_list, divisor)
print(divisible_tuples) 