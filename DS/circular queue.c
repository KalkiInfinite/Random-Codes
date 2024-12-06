#include <stdio.h>
#include <stdlib.h>

struct Queue {
    int data;
    struct Queue* next;
};

struct Queue *front = NULL;
struct Queue *rear = NULL;

void enqueue() {
    struct Queue *temp;
    temp = (struct Queue *)malloc(sizeof(struct Queue));
    printf("Enter value you want to enqueue: \t");
    scanf("%d", &temp->data);

    if (rear == NULL) {
        front = temp;
        rear = temp;
        rear->next = front;  // Circular link
    } else {
        rear->next = temp;
        rear = temp;
        rear->next = front;  // Circular link
    }
    puts("");  // Newline for better readability
}

void dequeue() {
    if (front == NULL) {
        puts("UNDERFLOW !!");
        return;
    }

    printf("Deleted value: %d\n", front->data);
    struct Queue *temp = front;

    if (rear == front) {
        // Only one element in the queue
        front = NULL;
        rear = NULL;
    } else {
        front = front->next;
        rear->next = front;  // Update rear to point to the new front
    }

    free(temp);  // Free the memory
}

void display() {
    if (front == NULL) {
        puts("UNDERFLOW !!");
        return;
    }

    struct Queue *temp = front;
    printf("List entered are: \n");

    do {
        printf("%d \t", temp->data);
        temp = temp->next;
    } while (temp != front);  // Loop until we get back to the front

    printf("\n");
}

int main() {
    int choice, y = 1;

    puts("CIRCULAR QUEUE USING LINKED LIST:");

    while (y) {
        puts("Enter 1 to ENQUEUE.");
        puts("Enter 2 to DEQUEUE.");
        puts("Enter 3 to DISPLAY.");
        puts("Enter 4 to EXIT.");
        printf("OPTION: \t");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                enqueue();
                break;
            case 2:
                dequeue();
                break;
            case 3:
                display();
                break;
            case 4:
                y = 0;
                break;
            default:
                printf("Enter Valid Input.\n");
        }
    }

    puts("You have exited the loop.");
    return 0;
}
