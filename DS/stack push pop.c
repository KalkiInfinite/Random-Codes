#include <stdio.h>
#define MAX_SIZE 100

struct Stack {
    int arr[MAX_SIZE];
    int top;
};

void initializeStack(struct Stack *stack) {
    stack->top = -1;
}

int isEmpty(struct Stack *stack) {
    return stack->top == -1;
}

int isFull(struct Stack *stack) {
    return stack->top == MAX_SIZE - 1;
}

void push(struct Stack *stack, int value) {
    if (isFull(stack)) {
        printf("Stack Overflow!\n");
        return;
    }
    stack->arr[++stack->top] = value;
    printf("Pushed %d\n", value);
}

void pop(struct Stack *stack) {
    if (isEmpty(stack)) {
        printf("Stack Underflow!\n");
        return;
    }
    printf("Popped %d\n", stack->arr[stack->top--]);
}

int main() {
    struct Stack stack;
    initializeStack(&stack);
    push(&stack, 5);
    push(&stack, 10);
    push(&stack, 15);
    pop(&stack);
    pop(&stack);
    pop(&stack);
    pop(&stack);
    return 0;
}
