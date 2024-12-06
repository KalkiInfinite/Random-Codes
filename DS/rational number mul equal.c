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

Rational multiply(const Rational *num1, const Rational *num2) {
    Rational result;
    result.numerator = num1->numerator * num2->numerator;
    result.denominator = num1->denominator * num2->denominator;
    simplify(&result);
    return result;
}

int isEqual(const Rational *num1, const Rational *num2) {
    return (num1->numerator == num2->numerator) && (num1->denominator == num2->denominator);
}

void display(const Rational *num) {
    printf("%d/%d\n", num->numerator, num->denominator);
}

int main() {
    Rational num1 = {3, 4};
    Rational num2 = {2, 3};
    printf("Number 1: ");
    display(&num1);
    printf("Number 2: ");
    display(&num2);
    printf("Multiplication: ");
    display(&multiply(&num1, &num2));
    if (isEqual(&num1, &num2)) {
        printf("Numbers are equal.\n");
    } else {
        printf("Numbers are not equal.\n");
    }
    return 0;
}
