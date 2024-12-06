import random

n = int(input("Enter size of an array: "))
ranarr = [random.randint(1, 50) for _ in range(n)]
ranarr.sort()
print("Randomly generated array:", ranarr)

key = int(input("Enter the value you want to search: "))

def binary_search(arr, key, imin, imax):
    swaps = 0
    while imin <= imax:
        imid = (imin + imax) // 2
        if arr[imid] < key:
            imin = imid + 1
        elif arr[imid] > key:
            imax = imid - 1
        else:
            return imid, swaps
        swaps += 1
    return -1, swaps

res, total_swaps = binary_search(ranarr, key, 0, len(ranarr) - 1)
print(f'Index of {key} is {res}')
print("Total number of comparisons during binary search:", total_swaps)
