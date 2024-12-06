import random
n = int(input("Enter size of an array : "))
ranarr = [random.randint(1, 50) for _ in range(n)]
ranarr.sort()  # For Best Case
ranarr.sort(reverse=True)  # For Worst Case
print("Randomly generated array", ranarr)

def insertionSort(ranarr):
    swap = 0
    n = len(ranarr)
    if n <= 1:
        return swap
    for j in range(1, n):
        key = ranarr[j]
        i = j - 1
        while i >= 0 and ranarr[i] > key:
            ranarr[i + 1] = ranarr[i]
            i -= 1
            swap += 1
        ranarr[i + 1] = key
    return swap

swapping = insertionSort(ranarr)
print("Array after sorting", ranarr)
print("Total no. of swaps", swapping)
