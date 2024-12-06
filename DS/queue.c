#include <stdio.h>
#include <stdlib.h>

struct Queue {
    int data;
    struct Queue* next;
};

struct Queue* front = NULL;
struct Queue* rear = NULL;

void enqueue() {
    struct Queue* temp;
    temp = (struct Queue*)malloc(sizeof(struct Queue));
    printf("Enter value you want to enqueue: \t");
    scanf("%d", &temp->data);

    if (rear == NULL) {
        front = temp;
        rear = temp;
    } else {
        rear->next = temp;
        rear = temp;
    }
    rear->next = NULL;
    puts("");
}

void dequeue() {
    if (front == NULL) {
        puts("UNDERFLOW !!");
    } else {
        printf("Deleted value: %d \n", front->data);
        struct Queue* temp = front;
        front = front->next;
        free(temp);
    }
}

void display() {
    if (front == NULL) {
        puts("Queue is EMPTY!");
    } else {
        struct Queue* temp = front;
        printf("Queue elements are: \n");
        while (temp != NULL) {
            printf("%d \t", temp->data);
            temp = temp->next;
        }
        puts("");
    }
}

int main() {
    int choice, y = 1;
    puts("QUEUE USING LINKED LIST:");

    while (y) {
        puts("Enter 1 to ENQUEUE.");
        puts("Enter 2 to DEQUEUE.");
        puts("Enter 3 to DISPLAY.");
        puts("Enter 4 to EXIT.");
        printf("OPTION: \t");
        scanf("%d", &choice);

        switch (choice) {
            case 1: {
                enqueue();
                break;
            }
            case 2: {
                dequeue();
                break;
            }
            case 3: {
                display();
                break;
            }
            case 4: {
                y = 0;
                break;
            }
            default: {
                printf("Enter a valid input.\n");
            }
        }
    }

    puts("You have exited the loop.");
    return 0;
}
