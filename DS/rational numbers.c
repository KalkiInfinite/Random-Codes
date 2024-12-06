#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int numerator;
    int denominator;
} Rational;

int gcd(int n1, int n2) {
    if (n2 == 0) {
        return n1;
    } else {
        return gcd(n2, n1 % n2);
    }
}

Rational format(Rational n) {
    if (n.numerator != 0) {
        int divisor = gcd(abs(n.numerator), abs(n.denominator));
        if (n.numerator * n.denominator > 0) {
            n.numerator = abs(n.numerator) / divisor;
            n.denominator = abs(n.denominator) / divisor;
        } else {
            n.numerator = -abs(n.numerator) / divisor;
            n.denominator = abs(n.denominator) / divisor;
        }
    }
    return n;
}

Rational input() {
    Rational n;
    printf("\nEnter numerator: ");
    scanf("%d", &n.numerator);
    printf("Enter denominator: ");
    scanf("%d", &n.denominator);
    if (n.denominator == 0) {
        printf("Error: Denominator cannot be zero. Please try again.\n");
        return input();
    }
    return format(n);
}

void text(Rational n) {
    if (n.numerator == 0) {
        printf("(0)");
    } else if (abs(n.numerator) < abs(n.denominator)) {
        printf("(%d/%d)", n.numerator, n.denominator);
    } else {
        int quotient = n.numerator / n.denominator;
        int remainder = abs(n.numerator % n.denominator);

        if (remainder == 0) {
            printf("(%d)", quotient);
        } else {
            printf("(%d + %d/%d)", quotient, remainder, abs(n.denominator));
        }
    }
}

Rational add(Rational n1, Rational n2) {
    Rational n;
    n.numerator = n1.numerator * n2.denominator + n2.numerator * n1.denominator;
    n.denominator = n1.denominator * n2.denominator;
    return format(n);
}

Rational subtract(Rational n1, Rational n2) {
    Rational n;
    n.numerator = n1.numerator * n2.denominator - n2.numerator * n1.denominator;
    n.denominator = n1.denominator * n2.denominator;
    return format(n);
}

Rational multiply(Rational n1, Rational n2) {
    Rational n;
    n.numerator = n1.numerator * n2.numerator;
    n.denominator = n1.denominator * n2.denominator;
    return format(n);
}

int equal(Rational n1, Rational n2) {
    return n1.numerator == n2.numerator && n1.denominator == n2.denominator;
}

int main() {
    Rational n1, n2, sum, difference, product;
    int equality, choice;

    while (1) {
        printf("\n\n0: EXIT\n1: ADDITION\n2: SUBTRACTION\n3: MULTIPLICATION\n4: EQUALITY\n\nEnter choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 0:
                printf("\nProgram successfully terminated.\n");
                exit(0);

            case 1:
                n1 = input();
                n2 = input();
                sum = add(n1, n2);
                text(n1);
                printf(" + ");
                text(n2);
                printf(" = ");
                text(sum);
                printf("\n");
                break;

            case 2:
                n1 = input();
                n2 = input();
                difference = subtract(n1, n2);
                text(n1);
                printf(" - ");
                text(n2);
                printf(" = ");
                text(difference);
                printf("\n");
                break;

            case 3:
                n1 = input();
                n2 = input();
                product = multiply(n1, n2);
                text(n1);
                printf(" * ");
                text(n2);
                printf(" = ");
                text(product);
                printf("\n");
                break;

            case 4:
                n1 = input();
                n2 = input();
                equality = equal(n1, n2);
                if (equality) {
                    text(n1);
                    printf(" = ");
                    text(n2);
                } else {
                    text(n1);
                    printf(" != ");
                    text(n2);
                }
                printf("\n");
                break;

            default:
                printf("Error: Invalid choice. Try again.\n");
        }
    }

    return 0;
}
