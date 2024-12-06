#include <stdio.h>
#include <stdlib.h>

struct StackNode {
    int data;
    struct StackNode* next;
};

struct StackNode* createNode(int data) {
    struct StackNode* node = (struct StackNode*)malloc(sizeof(struct StackNode));
    node->data = data;
    node->next = NULL;
    return node;
}

int isEmpty(struct StackNode* root) {
    return root == NULL;
}

void push(struct StackNode** root, int data) {
    struct StackNode* node = createNode(data);
    node->next = *root;
    *root = node;
}

int pop(struct StackNode** root) {
    struct StackNode* temp = *root;
    int popped = temp->data;
    *root = (*root)->next;
    free(temp);
    return popped;
}

void reverseList(int arr[], int size) {
    struct StackNode* stack = NULL;
    for (int i = 0; i < size; ++i) push(&stack, arr[i]);
    for (int i = 0; i < size; ++i) arr[i] = pop(&stack);
}

void displayList(int arr[], int size) {
    for (int i = 0; i < size; ++i) printf("%d ", arr[i]);
    printf("\n");
}

int main() {
    int numbers[] = {1, 2, 3, 4, 5};
    int size = sizeof(numbers) / sizeof(numbers[0]);
    displayList(numbers, size);
    reverseList(numbers, size);
    displayList(numbers, size);
    return 0;
}
