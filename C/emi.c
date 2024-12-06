#include <stdio.h>
#include <math.h>

int main() {
    float p, r, t, emi;
    int n;
    printf("Enter principal amount: ");
    scanf("%f", &p);
    printf("Enter annual interest rate: ");
    scanf("%f", &r);
    printf("Enter time in years: ");
    scanf("%f", &t);
    r = r / (12 * 100);
    n = t * 12;
    emi = p * r * pow((1+r), n) / (pow((1+r), n)-1);
    printf("Your monthly EMI is : %f", emi);
    return 0;
}