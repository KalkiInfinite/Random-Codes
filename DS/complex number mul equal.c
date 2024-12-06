#include <stdio.h>
typedef struct {
    float real;
    float imaginary;
} Complex;

Complex multiply(const Complex *num1, const Complex *num2) {
    Complex result;
    result.real = (num1->real * num2->real) - (num1->imaginary * num2->imaginary);
    result.imaginary = (num1->real * num2->imaginary) + (num1->imaginary * num2->real);
    return result;
}

int isEqual(const Complex *num1, const Complex *num2) {
    return (num1->real == num2->real) && (num1->imaginary == num2->imaginary);
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
    printf("Multiplication: ");
    display(&multiply(&num1, &num2));
    if (isEqual(&num1, &num2)) {
        printf("Numbers are equal.\n");
    } else {
        printf("Numbers are not equal.\n");
    }
    return 0;
}
