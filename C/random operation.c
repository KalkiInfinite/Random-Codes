#include <stdio.h>

int main() {
    int select;
    do {
        int num, remainder, rev = 0, orig, i, n, term, term1, term2, s = 0, sum = 0;

        printf("Press 1 for Palindrome\n");
        printf("Press 2 for Fibonacci series\n");
        printf("Press 3 to find the numbers and sum of all integers between 100 and 200 that are divisible by both 3 & 5\n");
        printf("Press 4 to EXIT!!\n");
        printf("\nENTER YOUR CHOICE BETWEEN 1-4: ");
        scanf("%d", &select);

        switch (select) {
            case 1: {
                printf("Enter the number you want to check for PALINDROME: ");
                scanf("%d", &num);
                orig = num;

                while (num > 0) {
                    remainder = num % 10;
                    rev = rev * 10 + remainder;
                    num = num / 10;
                }

                if (orig == rev) {
                    printf("\n\nIt's a palindrome number\n\n");
                } else {
                    printf("\n\nIt's not a palindrome\n\n");
                }
                break;
            }

            case 2: {
                printf("Enter the number of terms for the Fibonacci series: ");
                scanf("%d", &n);

                term = 0;
                term1 = 1;
                term2 = 1;

                printf("Fibonacci series: ");
                for (i = 1; i <= n; i++) {
                    printf("%d  ", term);
                    term = term1;
                    term1 = term2;
                    term2 = term + term1;
                    s += term;
                }
                printf("\nSum of Fibonacci series: %d\n", s);
                break;
            }

            case 3: {
                printf("Numbers divisible by 3 and 5 between 100 and 200:\n");
                for (int yum = 100; yum <= 200; yum++) {
                    if (yum % 3 == 0 && yum % 5 == 0) {
                        printf("%d\n", yum);
                        sum += yum;
                    }
                }
                printf("\nSum of all such numbers: %d\n\n", sum);
                break;
            }

            case 4: {
                printf("\n\nYOU HAVE EXITED THE MENU SUCCESSFULLY...!!\n");
                break;
            }

            default:
                printf("Please enter a valid number between 1 and 4.\n");
                break;
        }
    } while (select != 4);

    return 0;
}
