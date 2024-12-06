#include<stdio.h>
#include<stdlib.h>

void create();
void display();
void insert();
void delete();

struct node {
    int Exp2;
    struct node* next;
};

struct node *start = NULL;

int main() {
    int choice;
    while(1) {
        printf("\n 1. CREATE \n");
        printf("\n 2. DISPLAY \n");
        printf("\n 3. INSERT \n");
        printf("\n 4. DELETE \n");
        printf("\n 5. EXIT \n");
        printf("\n Enter your choice : \n");
        scanf("%d", &choice);

        switch(choice) {
            case 1 : create(); break;
            case 2 : display(); break;
            case 3 : insert(); break;
            case 4 : delete(); break;
            case 5 : exit(0); break;
            default : printf("Invalid Input");
        }
    }
    return 0;
}

void create() {
    struct node *temp, *ptr;
    temp = (struct node *)malloc(sizeof(struct node));
    printf("\n Enter the value of node \n");
    scanf("%d", &temp->Exp2);
    temp->next = NULL;

    if (start == NULL) {
        start = temp;
    } else {
        ptr = start;
        while(ptr->next != NULL) {
            ptr = ptr->next;
        }
        ptr->next = temp;
    }
}

void display() {
    struct node *ptr;
    if (start == NULL) {
        printf("\n List is empty \n");
        return;
    } else {
        ptr = start;
        printf("\n The elements are \n");
        while(ptr != NULL) {
            printf("\n %d \n", ptr->Exp2);
            ptr = ptr->next;
        }
    }
}

void insert() {
    struct node *temp, *ptr;
    temp = (struct node *)malloc(sizeof(struct node));
    printf("\n Enter the value of node \n");
    scanf("%d", &temp->Exp2);
    temp->next = NULL;

    if (start == NULL) {
        start = temp;
    } else {
        temp->next = start;
        start = temp;
    }
}

void delete() {
    int i, position;
    struct node *temp, *ptr;
    printf("\n Enter the position of node to be deleted \n");
    scanf("%d", &position);

    if(position == 0) {
        ptr = start;
        start = start->next;
        printf("\n Deleted element is: %d \n", ptr->Exp2);
        free(ptr);
    } else {
        ptr = start;
        for(i = 0; i < position; i++) {
            temp = ptr;
            ptr = ptr->next;
        }
        temp->next = ptr->next;
        printf("\n Deleted element is: %d \n", ptr->Exp2);
        free(ptr);
    }
}
