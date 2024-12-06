def list_operations(lst_1, lst_2):
    intersection = list(filter(lambda x: x in lst_2, lst_1))
    lst_1_minus_lst_2 = list(filter(lambda x: x not in lst_2, lst_1))
    lst_2_minus_lst_1 = list(filter(lambda x: x not in lst_1, lst_2))
    union = list(set(lst_1 + lst_2))
    return intersection, lst_1_minus_lst_2, lst_2_minus_lst_1, union

list_1 = [1, 2, 3, 4, 5]
list_2 = [3, 4, 5, 6, 7]
intersection_result, list_1_minus_list_2, list_2_minus_list_1, union_result = list_operations(list_1, list_2)
print("Intersection:", intersection_result)
print("List 1 - List 2:", list_1_minus_list_2)
print("List 2 - List 1:", list_2_minus_list_1)
print("Union:", union_result)