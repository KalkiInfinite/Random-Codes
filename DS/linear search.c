#include <stdio.h>
#include <stdlib.h>

int main() {
    int num;
    int a[10] = {2, 4, 7, 10, 11, 18, 12, 28, 27, 0};
    int found = 0;

    printf("Enter the number you want to search: ");
    scanf("%d", &num);

    for (int i = 0; i < 10; i++) {
        if (a[i] == num) {
            printf("The number %d is found at position %d.\n", num, i + 1);
            found = 1; // Mark as found
            break;
        }
    }

    if (!found) {
        printf("The number %d is not in the array.\n", num);
    }

    return 0;
}
