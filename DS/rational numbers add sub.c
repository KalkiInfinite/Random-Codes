#include <stdio.h>
typedef struct {
    int numerator;
    int denominator;
} Rational;

int gcd(int a, int b) {
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

void simplify(Rational *num) {
    int common_divisor = gcd(num->numerator, num->denominator);
    num->numerator /= common_divisor;
    num->denominator /= common_divisor;
}

Rational add(const Rational *num1, const Rational *num2) {
    Rational result;
    result.numerator = (num1->numerator * num2->denominator) + (num2->numerator * num1->denominator);
    result.denominator = num1->denominator * num2->denominator;
    simplify(&result);
    return result;
}

Rational subtract(const Rational *num1, const Rational *num2) {
    Rational result;
    result.numerator = (num1->numerator * num2->denominator) - (num2->numerator * num1->denominator);
    result.denominator = num1->denominator * num2->denominator;
    simplify(&result);
    return result;
}

void display(const Rational *num) {
    printf("%d/%d\n", num->numerator, num->denominator);
}

int main() {
    Rational num1 = {3, 4};
    Rational num2 = {1, 2};
    printf("Number 1: ");
    display(&num1);
    printf("Number 2: ");
    display(&num2);
    printf("Addition: ");
    display(&add(&num1, &num2));
    printf("Subtraction: ");
    display(&subtract(&num1, &num2));
    return 0;
}
