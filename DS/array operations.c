#include <stdio.h>

void insertion(int arr[], int *size, int index, int value) {
    if (index < 0 || index > *size) {
        printf("Error: Invalid index.\n");
        return;
    }

    for (int i = *size; i > index; i--) {
        arr[i] = arr[i - 1];
    }

    arr[index] = value;
    (*size)++;
}

void deletion(int arr[], int *size, int index) {
    if (index < 0 || index >= *size) {
        printf("Error: Invalid index.\n");
        return;
    }

    for (int i = index; i < *size - 1; i++) {
        arr[i] = arr[i + 1];
    }

    (*size)--;
}

int main() {
    int arr[10] = {1, 2, 3, 4};
    int size = 4;
    int value, index;

    printf("Original array: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }

    value = 5;
    index = 2;
    insertion(arr, &size, index, value);
    printf("\nArray after insertion: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }

    index = 3;
    deletion(arr, &size, index);
    printf("\nArray after deletion: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}
