#include <stdio.h>
typedef struct {
    float real;
    float imaginary;
} Complex;

Complex add(const Complex *num1, const Complex *num2) {
    Complex result;
    result.real = num1->real + num2->real;
    result.imaginary = num1->imaginary + num2->imaginary;
    return result;
}

Complex subtract(const Complex *num1, const Complex *num2) {
    Complex result;
    result.real = num1->real - num2->real;
    result.imaginary = num1->imaginary - num2->imaginary;
    return result;
}

void display(const Complex *num) {
    printf("%.2f + %.2fi\n", num->real, num->imaginary);
}

int main() {
    Complex num1 = {2.5, 3.0};
    Complex num2 = {1.5, 2.0};
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
