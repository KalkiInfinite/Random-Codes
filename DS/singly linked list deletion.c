#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

void append(struct Node** headRef, int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = NULL;
    if (*headRef == NULL) {
        *headRef = newNode;
    } else {
        struct Node* current = *headRef;
        while (current->next != NULL) {
            current = current->next;
        }
        current->next = newNode;
    }
}

void deleteFirst(struct Node** headRef) {
    if (*headRef == NULL) {
        printf("Cannot delete from an empty list.\n");
        return;
    }
    struct Node* temp = *headRef;
    *headRef = (*headRef)->next;
    free(temp);
}

void deleteLast(struct Node** headRef) {
    if (*headRef == NULL) {
        printf("Cannot delete from an empty list.\n");
        return;
    }
    if ((*headRef)->next == NULL) {
        free(*headRef);
        *headRef = NULL;
        return;
    }
    struct Node* current = *headRef;
    struct Node* prev = NULL;
    while (current->next != NULL) {
        prev = current;
        current = current->next;
    }
    free(current);
    prev->next = NULL;
}

void deleteAtPosition(struct Node** headRef, int position) {
    if (*headRef == NULL) {
        printf("Cannot delete from an empty list.\n");
        return;
    }
    if (position == 1) {
        deleteFirst(headRef);
        return;
    }
    struct Node* current = *headRef;
    struct Node* prev = NULL;
    int count = 1;
    while (current != NULL && count < position) {
        prev = current;
        current = current->next;
        ++count;
    }
    if (current == NULL) {
        printf("Invalid position for deletion.\n");
        return;
    }
    prev->next = current->next;
    free(current);
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
    append(&myList, 1);
    append(&myList, 2);
    append(&myList, 3);
    append(&myList, 4);
    printf("Original Linked List: ");
    display(myList);
    deleteFirst(&myList);
    printf("After deleting first element: ");
    display(myList);
    deleteLast(&myList);
    printf("After deleting last element: ");
    display(myList);
    deleteAtPosition(&myList, 2);
    printf("After deleting element at position 2: ");
    display(myList);
    return 0;
}
