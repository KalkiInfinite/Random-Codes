#include <stdio.h>
#include <studio.h>

int main() {
    int n1, n2, n3; 
    printf("Enter three different numbers: ");
    scanf("%d %d %d", &n1, &n2, &n3);

    if (n1 >= n2 && n1 >= n3)
        printf("%d is the largest number.\n", n1);
    else if (n2 >= n1 && n2 >= n3)
        printf("%d is the largest number.\n", n2); 
    else if (n3 >= n1 && n3 >= n2)
        printf("%d is the largest number.\n", n3);
    else
        printf("Entered value isnt a number \n");
    
    return 0;
}