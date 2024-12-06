import random
n = int(input("Enter size of an array : "))
ranarr = [random.randint(1, 50) for _ in range(n)]
print("Randomly generated array", ranarr)

def SelectionSort(arr):
    n = len(arr)
    count = 0
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            count = count + 1
    return count

swapping = SelectionSort(ranarr)
print("Array after sorting", ranarr)
print("Total no. of swaps", swapping)
