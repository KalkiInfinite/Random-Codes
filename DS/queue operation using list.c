#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct CircularQueue {
    struct Node* front;
    struct Node* rear;
};

struct PriorityQueue {
    struct Node* front;
};

struct DoubleEndedQueue {
    struct Node* front;
    struct Node* rear;
};

struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (newNode == NULL) {
        printf("Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

void initCircularQueue(struct CircularQueue* cq) {
    cq->front = cq->rear = NULL;
}

void initPriorityQueue(struct PriorityQueue* pq) {
    pq->front = NULL;
}

void initDoubleEndedQueue(struct DoubleEndedQueue* deq) {
    deq->front = deq->rear = NULL;
}

int isCircularQueueEmpty(struct CircularQueue* cq) {
    return (cq->front == NULL);
}

int isPriorityQueueEmpty(struct PriorityQueue* pq) {
    return (pq->front == NULL);
}

int isDoubleEndedQueueEmpty(struct DoubleEndedQueue* deq) {
    return (deq->front == NULL);
}

void enqueueCircularQueue(struct CircularQueue* cq, int value) {
    struct Node* newNode = createNode(value);
    if (isCircularQueueEmpty(cq)) {
        cq->front = cq->rear = newNode;
    } else {
        cq->rear->next = newNode;
        cq->rear = newNode;
    }
    cq->rear->next = cq->front;
    printf("Inserted %d into the circular queue\n", value);
}

void dequeueCircularQueue(struct CircularQueue* cq) {
    if (isCircularQueueEmpty(cq)) {
        printf("Queue is empty. Cannot delete element\n");
        return;
    }
    struct Node* temp = cq->front;
    if (cq->front == cq->rear) {
        cq->front = cq->rear = NULL;
    } else {
        cq->front = cq->front->next;
        cq->rear->next = cq->front;
    }
    printf("Deleted %d from the circular queue\n", temp->data);
    free(temp);
}

void enqueuePriorityQueue(struct PriorityQueue* pq, int value) {
    struct Node* newNode = createNode(value);
    if (isPriorityQueueEmpty(pq) || value < pq->front->data) {
        newNode->next = pq->front;
        pq->front = newNode;
    } else {
        struct Node* current = pq->front;
        while (current->next != NULL && value >= current->next->data) {
            current = current->next;
        }
        newNode->next = current->next;
        current->next = newNode;
    }
    printf("Inserted %d into the priority queue\n", value);
}

void dequeuePriorityQueue(struct PriorityQueue* pq) {
    if (isPriorityQueueEmpty(pq)) {
        printf("Queue is empty. Cannot delete element\n");
        return;
    }
    struct Node* temp = pq->front;
    pq->front = pq->front->next;
    printf("Deleted %d from the priority queue\n", temp->data);
    free(temp);
}

void enqueueFrontDoubleEndedQueue(struct DoubleEndedQueue* deq, int value) {
    struct Node* newNode = createNode(value);
    if (isDoubleEndedQueueEmpty(deq)) {
        deq->front = deq->rear = newNode;
    } else {
        newNode->next = deq->front;
        deq->front = newNode;
    }
    printf("Inserted %d at the front of the double-ended queue\n", value);
}

void enqueueRearDoubleEndedQueue(struct DoubleEndedQueue* deq, int value) {
    struct Node* newNode = createNode(value);
    if (isDoubleEndedQueueEmpty(deq)) {
        deq->front = deq->rear = newNode;
    } else {
        deq->rear->next = newNode;
        deq->rear = newNode;
    }
    printf("Inserted %d at the rear of the double-ended queue\n", value);
}

void dequeueFrontDoubleEndedQueue(struct DoubleEndedQueue* deq) {
    if (isDoubleEndedQueueEmpty(deq)) {
        printf("Queue is empty. Cannot delete element from the front\n");
        return;
    }
    struct Node* temp = deq->front;
    if (deq->front == deq->rear) {
        deq->front = deq->rear = NULL;
    } else {
        deq->front = deq->front->next;
    }
    printf("Deleted %d from the front of the double-ended queue\n", temp->data);
    free(temp);
}

void dequeueRearDoubleEndedQueue(struct DoubleEndedQueue* deq) {
    if (isDoubleEndedQueueEmpty(deq)) {
        printf("Queue is empty. Cannot delete element from the rear\n");
        return;
    }
    struct Node* temp = deq->front;
    if (deq->front == deq->rear) {
        deq->front = deq->rear = NULL;
    } else {
        while (temp->next != deq->rear) {
            temp = temp->next;
        }
        temp->next = NULL;
        deq->rear = temp;
    }
    printf("Deleted %d from the rear of the double-ended queue\n", deq->rear->data);
    free(deq->rear);
}

void displayCircularQueue(struct CircularQueue* cq) {
    if (isCircularQueueEmpty(cq)) {
        printf("Queue is empty\n");
        return;
    }
    struct Node* current = cq->front;
    do {
        printf("%d ", current->data);
        current = current->next;
    } while (current != cq->front);
    printf("\n");
}

void displayPriorityQueue(struct PriorityQueue* pq) {
    if (isPriorityQueueEmpty(pq)) {
        printf("Queue is empty\n");
        return;
    }
    struct Node* current = pq->front;
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
}

void displayDoubleEndedQueue(struct DoubleEndedQueue* deq) {
    if (isDoubleEndedQueueEmpty(deq)) {
        printf("Queue is empty\n");
        return;
    }
    struct Node* current = deq->front;
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
}

int main() {
    struct CircularQueue circularQueue;
    initCircularQueue(&circularQueue);
    printf("Circular Queue Operations:\n");
    enqueueCircularQueue(&circularQueue, 1);
    enqueueCircularQueue(&circularQueue, 2);
    enqueueCircularQueue(&circularQueue, 3);
    displayCircularQueue(&circularQueue);
    dequeueCircularQueue(&circularQueue);
    displayCircularQueue(&circularQueue);
    printf("\n");

    struct PriorityQueue priorityQueue;
    initPriorityQueue(&priorityQueue);
    printf("Priority Queue Operations:\n");
    enqueuePriorityQueue(&priorityQueue, 3);
    enqueuePriorityQueue(&priorityQueue, 1);
    enqueuePriorityQueue(&priorityQueue, 2);
    displayPriorityQueue(&priorityQueue);
    dequeuePriorityQueue(&priorityQueue);
    displayPriorityQueue(&priorityQueue);
    printf("\n");

    struct DoubleEndedQueue doubleEndedQueue;
    initDoubleEndedQueue(&doubleEndedQueue);
    printf("Double Ended Queue Operations:\n");
    enqueueFrontDoubleEndedQueue(&doubleEndedQueue, 1);
    enqueueRearDoubleEndedQueue(&doubleEndedQueue, 2);
    enqueueFrontDoubleEndedQueue(&doubleEndedQueue, 3);
    displayDoubleEndedQueue(&doubleEndedQueue);
    dequeueFrontDoubleEndedQueue(&doubleEndedQueue);
    displayDoubleEndedQueue(&doubleEndedQueue);
    return 0;
}
