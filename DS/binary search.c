#include <stdio.h>
#include <stdlib.h>

int main() {
    int num;
    int a[10] = {0, 2, 4, 7, 10, 11, 12, 18, 27, 28}; 

    printf("Enter the number you want to search: ");
    scanf("%d", &num);

    int low = 0, high = 9;
    int found = 0;

    while (low <= high) {
        int mid = (low + high) / 2;

        if (a[mid] == num) {
            printf("The number %d is found at position %d.\n", num, mid + 1);
            found = 1; 
            break;
        } else if (a[mid] < num) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    if (!found) {
        printf("The number %d is not in the array.\n", num);
    }

    return 0;
}
