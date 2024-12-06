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

void deleteFirst(struct Node** headRef) {
    if (*headRef == NULL) {
        printf("Cannot delete from an empty list.\n");
        return;
    }
    struct Node* temp = *headRef;
    *headRef = (*headRef)->next;
    if (*headRef != NULL) {
        (*headRef)->prev = NULL;
    }
    free(temp);
}

void deleteLast(struct Node** headRef) {
    if (*headRef == NULL) {
        printf("Cannot delete from an empty list.\n");
        return;
    }
    struct Node* current = *headRef;
    while (current->next != NULL) {
        current = current->next;
    }
    if (current->prev != NULL) {
        current->prev->next = NULL;
    } else {
        *headRef = NULL;
    }
    free(current);
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
    int count = 1;
    while (current != NULL && count < position) {
        current = current->next;
        ++count;
    }
    if (current == NULL) {
        printf("Invalid position for deletion.\n");
        return;
    }
    if (current->next != NULL) {
        current->next->prev = current->prev;
    }
    if (current->prev != NULL) {
        current->prev->next = current->next;
    }
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
    printf("Original Doubly Linked List: ");
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
