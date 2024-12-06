#include <stdio.h>

int main() {
    int select;
    do {
        int n1, n2, n3, n4;

        printf("Enter first number: ");
        scanf("%d", &n1);
        printf("Enter second number: ");
        scanf("%d", &n2);
        printf("Enter third number: ");
        scanf("%d", &n3);
        printf("Enter fourth number: ");
        scanf("%d", &n4);

        printf("\nMenu Options:\n");
        printf("Press 1 to Display the smallest number entered\n");
        printf("Press 2 to Display the largest number entered\n");
        printf("Press 3 to Display the sum of the four numbers entered\n");
        printf("Press 4 to Display the average of the four numbers entered\n");
        printf("Press 5 to EXIT!!\n");

        printf("\nEnter your choice (1-5): ");
        scanf("%d", &select);

        switch (select) {
            case 1: {
                int smallest = n1;

                if (n2 < smallest) smallest = n2;
                if (n3 < smallest) smallest = n3;
                if (n4 < smallest) smallest = n4;

                printf("\nSmallest: %d\n", smallest);
                break;
            }
            case 2: {
                int largest = n1;

                if (n2 > largest) largest = n2;
                if (n3 > largest) largest = n3;
                if (n4 > largest) largest = n4;

                printf("\nLargest: %d\n", largest);
                break;
            }
            case 3: {
                int sum = n1 + n2 + n3 + n4;
                printf("\nSum of the numbers: %d\n", sum);
                break;
            }
            case 4: {
                float average = (n1 + n2 + n3 + n4) / 4.0; // Use 4.0 for accurate floating-point division
                printf("\nAverage of the numbers: %.2f\n", average);
                break;
            }
            case 5: {
                printf("\n\nYOU HAVE EXITED THE MENU SUCCESSFULLY...!!\n");
                break;
            }
            default: {
                printf("\nInvalid choice! Please enter a number between 1 and 5.\n");
                break;
            }
        }
    } while (select != 5);

    return 0;
}
