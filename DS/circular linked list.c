#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

void append(struct Node** headRef, int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    if (*headRef == NULL) {
        *headRef = newNode;
        newNode->next = newNode;
    } else {
        struct Node* current = *headRef;
        while (current->next != *headRef) {
            current = current->next;
        }
        current->next = newNode;
        newNode->next = *headRef;
    }
}

void display(struct Node* head) {
    if (head == NULL) return;
    struct Node* current = head;
    do {
        printf("%d ", current->data);
        current = current->next;
    } while (current != head);
    printf("\n");
}

int main() {
    struct Node* myCircularList = NULL;
    append(&myCircularList, 1);
    append(&myCircularList, 2);
    append(&myCircularList, 3);
    append(&myCircularList, 4);
    display(myCircularList);
    return 0;
}
