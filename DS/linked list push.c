#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Stack {
    struct Node* top;
};

void initializeStack(struct Stack* stack) {
    stack->top = NULL;
}

int isEmpty(struct Stack* stack) {
    return stack->top == NULL;
}

void push(struct Stack* stack, int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = stack->top;
    stack->top = newNode;
    printf("Pushed %d\n", value);
}

void pop(struct Stack* stack) {
    if (isEmpty(stack)) {
        printf("Stack Underflow!\n");
        return;
    }
    struct Node* temp = stack->top;
    printf("Popped %d\n", temp->data);
    stack->top = temp->next;
    free(temp);
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
