#include <stdio.h>

int stack[100];
int stackvalue, tempvalue, top = -1;

void push();
void pop();
void display();
void peek();

int main() {
    printf("Enter value of stack (where max value is 100): \t");
    scanf("%d", &stackvalue);

    int choice, y = 1;
    printf("Enter 1 to PUSH. \nEnter 2 to POP.\nEnter 3 to DISPLAY.\nEnter 4 to PEEK.\nEnter 5 to EXIT.\n");

    while (y) {
        printf("OPTION: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1: {
                push();
                break;
            }
            case 2: {
                pop();
                break;
            }
            case 3: {
                display();
                break;
            }
            case 4: {
                peek();
                break;
            }
            case 5: {
                y = 0;
                break;
            }
            default: {
                printf("Enter Valid Input.\n");
            }
        }
    }

    printf("You have exited the loop.\n");
    return 0;
}

void push() {
    if (top >= stackvalue - 1) {
        printf("Error: STACK OVERFLOW!\n");
    } else {
        printf("Enter value you want to enter: \t");
        scanf("%d", &tempvalue);
        top++;
        stack[top] = tempvalue;
    }
    printf("\n");
}

void pop() {
    if (top <= -1) {
        printf("Error: STACK UNDERFLOW!\n");
    } else {
        printf("%d element is popped\n", stack[top]);
        top--;
    }
    printf("\n");
}

void display() {
    if (top >= 0) {
        printf("Elements in stack: ");
        for (int i = top; i >= 0; i--) {
            printf("%d \t", stack[i]);
        }
        printf("\n");
    } else {
        printf("Error: STACK EMPTY!\n");
    }
}

void peek() {
    if (top <= -1) {
        printf("Error: STACK UNDERFLOW!\n");
    } else {
        printf("Element at the top is %d\n", stack[top]);
    }
    printf("\n");
}
