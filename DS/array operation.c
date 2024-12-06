#include <stdio.h>

void displayArray(const int arr[], int size) {
    for (int i = 0; i < size; ++i) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void insertElement(int arr[], int *size, int element, int position) {
    if (position < 0 || position > *size) {
        printf("Invalid position for insertion.\n");
        return;
    }
    for (int i = *size - 1; i >= position; --i) {
        arr[i + 1] = arr[i];
    }
    arr[position] = element;
    ++*size;
}

void deleteElement(int arr[], int *size, int position) {
    if (position < 0 || position >= *size) {
        printf("Invalid position for deletion.\n");
        return;
    }
    for (int i = position; i < *size - 1; ++i) {
        arr[i] = arr[i + 1];
    }
    --*size;
}

int main() {
    const int maxSize = 100;
    int arr[maxSize];
    int size = 5;
    for (int i = 0; i < size; ++i) {
        arr[i] = i + 1;
    }
    printf("Original Array: ");
    displayArray(arr, size);
    insertElement(arr, &size, 10, 2);
    printf("After Insertion: ");
    displayArray(arr, size);
    deleteElement(arr, &size, 4);
    printf("After Deletion: ");
    displayArray(arr, size);
    return 0;
}
