#include <stdio.h>
#include <stdlib.h>

typedef struct {
    double re;
    double img;
} Complex;

Complex input() {
    Complex z;
    printf("\nEnter real part:  ");
    scanf("%lf", &z.re);
    printf("Enter imaginary part:  ");
    scanf("%lf", &z.img);
    return z;
}

void text(Complex z) {
    if (z.img >= 0) {
        printf("(%lf + %lfi)", z.re, z.img);
    } else {
        printf("(%lf - %lfi)", z.re, -z.img);
    }
}

Complex add(Complex z1, Complex z2) {
    Complex z;
    z.re = z1.re + z2.re;
    z.img = z1.img + z2.img;
    return z;
}

Complex subtract(Complex z1, Complex z2) {
    Complex z;
    z.re = z1.re - z2.re;
    z.img = z1.img - z2.img;
    return z;
}

Complex multiply(Complex z1, Complex z2) {
    Complex z;
    z.re = z1.re * z2.re - z1.img * z2.img;
    z.img = z1.re * z2.img + z1.img * z2.re;
    return z;
}

int equal(Complex z1, Complex z2) {
    return z1.re == z2.re && z1.img == z2.img;
}

int main() {
    Complex z1, z2, sum, difference, product;
    int equality, choice;

    while (1) {
        printf("\n\n0:  EXIT\n1:  ADDITION\n2:  SUBTRACTION\n3:  MULTIPLICATION\n4: EQUALITY\n\nEnter choice:  ");
        scanf("%d", &choice);

        switch (choice) {
            case 0:
                printf("\nProgram successfully terminated.\n");
                exit(0);
                break;

            case 1:
                z1 = input();
                z2 = input();
                sum = add(z1, z2);
                text(z1);
                printf(" + ");
                text(z2);
                printf(" = ");
                text(sum);
                printf("\n");
                break;

            case 2:
                z1 = input();
                z2 = input();
                difference = subtract(z1, z2);
                text(z1);
                printf(" - ");
                text(z2);
                printf(" = ");
                text(difference);
                printf("\n");
                break;

            case 3:
                z1 = input();
                z2 = input();
                product = multiply(z1, z2);
                text(z1);
                printf(" * ");
                text(z2);
                printf(" = ");
                text(product);
                printf("\n");
                break;

            case 4:
                z1 = input();
                z2 = input();
                equality = equal(z1, z2);
                if (equality) {
                    text(z1);
                    printf(" = ");
                    text(z2);
                } else {
                    text(z1);
                    printf(" != ");
                    text(z2);
                }
                printf("\n");
                break;

            default:
                printf("Error: Invalid choice. Try again.\n");
        }
    }

    return 0;
}
