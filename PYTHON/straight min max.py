import random

n = int(input("Enter size of an array: "))
ranarr = [random.randint(1, 50) for _ in range(n)]
print("Randomly generated array:", ranarr)

def straight_max_min(a):
    swap_count = 0
    max_val = min_val = a[0]
    for i in range(1, len(a)):
        if a[i] > max_val:
            max_val = a[i]
        if a[i] < min_val:
            min_val = a[i]
        swap_count += 1
    return max_val, min_val, swap_count

max_value, min_value, swapping = straight_max_min(ranarr)
print(f'Maximum value: {max_value}')
print(f'Minimum value: {min_value}')
print("Total no. of swaps:", swapping)
