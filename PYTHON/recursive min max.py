import random

n = int(input("Enter size of an array: "))
ranarr = [random.randint(1, 50) for _ in range(n)]
print("Randomly generated array:", ranarr)

def recursive_maxmin(i, j):
    swaps = 0
    if i == j:
        return ranarr[i], ranarr[i], 0
    elif i == j - 1:
        if ranarr[i] < ranarr[j]:
            return ranarr[j], ranarr[i], 1
        else:
            return ranarr[i], ranarr[j], 0
    else:
        mid = (i + j) // 2
        max1, min1, swap1 = recursive_maxmin(i, mid)
        max2, min2, swap2 = recursive_maxmin(mid + 1, j)
        max_val = max(max1, max2)
        min_val = min(min1, min2)
        total_swap = swap1 + swap2
        return max_val, min_val, total_swap

start_index = 0
end_index = len(ranarr) - 1
max_value, min_value, swapping = recursive_maxmin(start_index, end_index)
print(f'Maximum value: {max_value}')
print(f'Minimum value: {min_value}')
print("Total no. of swaps:", swapping)
