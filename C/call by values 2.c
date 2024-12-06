#include <stdio.h>

void main(){
    int A = 10;
    printf("Value of A is %d\n", A);
    printf("Address of A is %d\n", &A);
    int *P;
    P = &A;
    printf("Value of P is %d\n", P);
    printf("Address of P is %d\n", &P);
    printf("Value at the address in P is %d\n", *P);
    *P = 20;
    printf("New Value of A is %d\n", A);
}