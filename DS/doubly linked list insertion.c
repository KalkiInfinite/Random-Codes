#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
    struct Node* prev;
};

void append(struct Node** headRef, int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = NULL;
    if (*headRef == NULL) {
        *headRef = newNode;
        newNode->prev = NULL;
    } else {
        struct Node* current = *headRef;
        while (current->next != NULL) {
            current = current->next;
        }
        current->next = newNode;
        newNode->prev = current;
    }
}

void insertAtBeginning(struct Node** headRef, int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = *headRef;
    newNode->prev = NULL;
    if (*headRef != NULL) {
        (*headRef)->prev = newNode;
    }
    *headRef = newNode;
}

void insertAtEnd(struct Node** headRef, int value) {
    append(headRef, value);
}

void insertAtPosition(struct Node** headRef, int value, int position) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    if (position == 1) {
        insertAtBeginning(headRef, value);
        return;
    }
    struct Node* current = *headRef;
    int count = 1;
    while (current != NULL && count < position - 1) {
        current = current->next;
        ++count;
    }
    if (current == NULL) {
        printf("Invalid position for insertion.\n");
        return;
    }
    newNode->next = current->next;
    newNode->prev = current;
    if (current->next != NULL) {
        current->next->prev = newNode;
    }
    current->next = newNode;
}

void display(struct Node* head) {
    struct Node* current = head;
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
}

int main() {
    struct Node* myList = NULL;
    append(&myList, 2);
    append(&myList, 3);
    append(&myList, 4);
    printf("Original Doubly Linked List: ");
    display(myList);
    insertAtBeginning(&myList, 1);
    printf("After inserting 1 at the beginning: ");
    display(myList);
    insertAtEnd(&myList, 5);
    printf("After inserting 5 at the end: ");
    display(myList);
    insertAtPosition(&myList, 3, 2);
    printf("After inserting 3 at position 2: ");
    display(myList);
    return 0;
}
