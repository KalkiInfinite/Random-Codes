import random

def recursive_binary_search(arr, key, imin, imax, swaps):
    if imin <= imax:
        imid = (imin + imax) // 2
        if arr[imid] == key:
            return imid, swaps
        elif arr[imid] > key:
            return recursive_binary_search(arr, key, imin, imid - 1, swaps + 1)
        else:
            return recursive_binary_search(arr, key, imid + 1, imax, swaps + 1)
    return -1, swaps

n = int(input("Enter size of an array: "))
ranarr = [random.randint(1, 50) for _ in range(n)]
ranarr.sort()
print("Randomly generated array:", ranarr)

key = int(input("Enter the value you want to search: "))
res, total_swaps = recursive_binary_search(ranarr, key, 0, len(ranarr) - 1, 0)
print(f'Index of {key} is {res}')
print("Total number of comparisons during binary search:", total_swaps)
