def update_tuple_value(test_list, index, value):
    return [tuple(value if i == index else x for i, x in enumerate(t)) for t in test_list]

test_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
index = 1
new_value = 10
updated_list = update_tuple_value(test_list, index, new_value)
print(f"Original list: {test_list}")
print(f"Updated list: {updated_list}")