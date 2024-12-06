#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int stack[20];
int top = -1;

void push(int tempvalue);
int pop();
void postfixexpression();

int main() {
    int x = 1, y;
    printf("Enter 1 to calculate.\nEnter 0 to exit.\n");

    while (x == 1) {
        printf("Enter choice: \t");
        scanf("%d", &y);

        switch (y) {
            case 1: {
                postfixexpression();
                break;
            }
            case 0: {
                x = 0;
                break;
            }
            default: {
                printf("Invalid input. Please enter 1 to calculate or 0 to exit.\n");
                break;
            }
        }
    }

    printf("You have exited the loop.\nThank you!\n");
    return 0;
}

void push(int tempvalue) {
    if (top >= 19) {
        printf("Stack Overflow!\n");
        return;
    }
    top++;
    stack[top] = tempvalue;
}

int pop() {
    if (top < 0) {
        printf("Stack Underflow!\n");
        return -1;  // Return -1 in case of underflow, you could handle this case differently based on your logic.
    }
    int value = stack[top];
    top--;
    return value;
}

void postfixexpression() {
    char expression[20];
    char *ptr;
    int finalresult, temp, number1, number2;

    printf("Enter the postfix expression: ");
    scanf("%s", expression);
    ptr = expression;

    while (*ptr != '\0') {
        if (isdigit(*ptr)) {
            temp = *ptr - '0'; // Convert char to integer
            push(temp);
        } else {
            number2 = pop();
            number1 = pop();
            switch (*ptr) {
                case '+':
                    temp = number1 + number2;
                    break;
                case '-':
                    temp = number1 - number2;
                    break;
                case '*':
                    temp = number1 * number2;
                    break;
                case '/':
                    if (number2 != 0) {
                        temp = number1 / number2;
                    } else {
                        printf("Error: Division by zero!\n");
                        return;
                    }
                    break;
                case '%':
                    temp = number1 % number2;
                    break;
                default:
                    printf("Error: Invalid operator %c\n", *ptr);
                    return;
            }
            push(temp);
        }
        ptr++;
    }

    finalresult = pop();
    if (top == -1) {
        printf("Result of expression %s is %d\n", expression, finalresult);
    } else {
        printf("Error: Invalid postfix expression.\n");
    }
}
