#include <stdio.h>
#include <stdlib.h>

struct node {
    int Exp2;
    struct node *next;
    struct node *prev;
};

struct node *start = NULL;

void create();
void display();
void insert();
void delete();

int main() {
    int choice;
    while (1) {
        printf("\n 1. CREATE \n");
        printf("\n 2. DISPLAY \n");
        printf("\n 3. INSERT \n");
        printf("\n 4. DELETE \n");
        printf("\n 5. EXIT \n");
        printf("\n Enter your choice : \n");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                create();
                break;
            case 2:
                display();
                break;
            case 3:
                insert();
                break;
            case 4:
                delete();
                break;
            case 5:
                exit(0);
                break;
            default:
                printf("Invalid Input");
        }
    }
    return 0;
}

void create() {
    struct node *temp, *ptr;
    temp = (struct node *)malloc(sizeof(struct node));
    printf("\n Enter the value of node \n");
    scanf("%d", &temp->Exp2);
    temp->next = temp->prev = temp; // Point to itself for circular link
    if (start == NULL) {
        start = temp;
    } else {
        ptr = start;
        while (ptr->next != start) {
            ptr = ptr->next;
        }
        ptr->next = temp;
        temp->prev = ptr;
        temp->next = start;
        start->prev = temp;
    }
}

void display() {
    struct node *ptr;
    if (start == NULL) {
        printf("\n List is empty \n");
        return;
    }
    printf("\n The elements are \n");
    ptr = start;
    do {
        printf("\n %d \n", ptr->Exp2);
        ptr = ptr->next;
    } while (ptr != start);
}

void insert() {
    struct node *temp;
    temp = (struct node *)malloc(sizeof(struct node));
    printf("\n Enter the value of node \n");
    scanf("%d", &temp->Exp2);
    temp->next = temp->prev = temp; // Point to itself for circular link
    if (start == NULL) {
        start = temp;
    } else {
        temp->next = start;
        temp->prev = start->prev;
        start->prev->next = temp;
        start->prev = temp;
        start = temp; // Inserting at the beginning
    }
}

void delete() {
    int position;
    struct node *temp, *ptr;
    printf("\n Enter the position of node to be deleted \n");
    scanf("%d", &position);
    if (start == NULL) {
        printf("\n List is empty \n");
        return;
    }
    ptr = start;
    for (int i = 1; i < position; i++) {
        ptr = ptr->next;
        if (ptr == start) {
            printf("\n Invalid position \n");
            return;
        }
    }

    if (ptr->next == start) {
        // Deleting the last node
        ptr->prev->next = start;
        start->prev = ptr->prev;
        free(ptr);
    } else {
        // Deleting a node from middle
        ptr->prev->next = ptr->next;
        ptr->next->prev = ptr->prev;
        if (ptr == start) {
            start = ptr->next;
        }
        free(ptr);
    }
}
