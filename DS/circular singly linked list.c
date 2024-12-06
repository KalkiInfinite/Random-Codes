#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

void append(struct Node** headRef, int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = *headRef;
    if (*headRef == NULL) {
        *headRef = newNode;
        newNode->next = *headRef;
    } else {
        struct Node* current = *headRef;
        while (current->next != *headRef) {
            current = current->next;
        }
        current->next = newNode;
        newNode->next = *headRef;
    }
}

void deleteFirst(struct Node** headRef) {
    if (*headRef == NULL) {
        printf("Cannot delete from an empty list.\n");
        return;
    }
    struct Node* temp = *headRef;
    struct Node* current = *headRef;
    while (current->next != *headRef) {
        current = current->next;
    }
    *headRef = (*headRef)->next;
    current->next = *headRef;
    free(temp);
}

void deleteLast(struct Node** headRef) {
    if (*headRef == NULL) {
        printf("Cannot delete from an empty list.\n");
        return;
    }
    struct Node* current = *headRef;
    struct Node* prev = NULL;
    while (current->next != *headRef) {
        prev = current;
        current = current->next;
    }
    if (prev != NULL) {
        prev->next = *headRef;
    } else {
        *headRef = NULL;
    }
    free(current);
}

void display(struct Node* head) {
    if (head == NULL) {
        printf("List is empty.\n");
        return;
    }
    struct Node* current = head;
    do {
        printf("%d ", current->data);
        current = current->next;
    } while (current != head);
    printf("\n");
}

int main() {
    struct Node* myList = NULL;
    append(&myList, 1);
    append(&myList, 2);
    append(&myList, 3);
    append(&myList, 4);
    printf("Original Circular Singly Linked List: ");
    display(myList);
    deleteFirst(&myList);
    printf("After deleting first element: ");
    display(myList);
    deleteLast(&myList);
    printf("After deleting last element: ");
    display(myList);
    return 0;
}
