def filter_tuples(test_list, k):
    return [tup for tup in test_list if len(tup) != k]

test_list = [(1, 2, 3), (4, 5), (6, 7, 8, 9), (10,)]
k = 3
filtered_list = filter_tuples(test_list, k)
print(f"Original list: {test_list}")
print(f"Filtered list (tuples not of length {k}): {filtered_list}")