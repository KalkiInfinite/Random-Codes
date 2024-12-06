#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 5

struct CircularQueue {
    int front, rear;
    int arr[MAX_SIZE];
};

struct PriorityQueue {
    int front, rear;
    int arr[MAX_SIZE];
};

struct DoubleEndedQueue {
    int front, rear;
    int arr[MAX_SIZE];
};

void initCircularQueue(struct CircularQueue* cq) {
    cq->front = cq->rear = -1;
}

void initPriorityQueue(struct PriorityQueue* pq) {
    pq->front = pq->rear = -1;
}

void initDoubleEndedQueue(struct DoubleEndedQueue* deq) {
    deq->front = deq->rear = -1;
}

int isCircularQueueEmpty(struct CircularQueue* cq) {
    return (cq->front == -1 && cq->rear == -1);
}

int isPriorityQueueEmpty(struct PriorityQueue* pq) {
    return (pq->front == -1 && pq->rear == -1);
}

int isDoubleEndedQueueEmpty(struct DoubleEndedQueue* deq) {
    return (deq->front == -1 && deq->rear == -1);
}

int isCircularQueueFull(struct CircularQueue* cq) {
    return (cq->front == (cq->rear + 1) % MAX_SIZE);
}

int isPriorityQueueFull(struct PriorityQueue* pq) {
    return (pq->rear == MAX_SIZE - 1);
}

int isDoubleEndedQueueFull(struct DoubleEndedQueue* deq) {
    return ((deq->front == 0 && deq->rear == MAX_SIZE - 1) || (deq->front == deq->rear + 1));
}

void enqueueCircularQueue(struct CircularQueue* cq, int value) {
    if (isCircularQueueFull(cq)) {
        printf("Queue is full. Cannot insert element %d\n", value);
        return;
    }
    if (isCircularQueueEmpty(cq)) {
        cq->front = cq->rear = 0;
    } else {
        cq->rear = (cq->rear + 1) % MAX_SIZE;
    }
    cq->arr[cq->rear] = value;
    printf("Inserted %d into the circular queue\n", value);
}

void dequeueCircularQueue(struct CircularQueue* cq) {
    if (isCircularQueueEmpty(cq)) {
        printf("Queue is empty. Cannot delete element\n");
        return;
    }
    printf("Deleted %d from the circular queue\n", cq->arr[cq->front]);
    if (cq->front == cq->rear) {
        cq->front = cq->rear = -1;
    } else {
        cq->front = (cq->front + 1) % MAX_SIZE;
    }
}

void enqueuePriorityQueue(struct PriorityQueue* pq, int value) {
    if (isPriorityQueueFull(pq)) {
        printf("Queue is full. Cannot insert element %d\n", value);
        return;
    }
    if (isPriorityQueueEmpty(pq)) {
        pq->front = pq->rear = 0;
        pq->arr[pq->rear] = value;
    } else {
        int i = pq->rear;
        while (i >= 0 && value > pq->arr[i]) {
            pq->arr[i + 1] = pq->arr[i];
            i--;
        }
        pq->arr[i + 1] = value;
        pq->rear++;
    }
    printf("Inserted %d into the priority queue\n", value);
}

void dequeuePriorityQueue(struct PriorityQueue* pq) {
    if (isPriorityQueueEmpty(pq)) {
        printf("Queue is empty. Cannot delete element\n");
        return;
    }
    printf("Deleted %d from the priority queue\n", pq->arr[pq->front]);
    if (pq->front == pq->rear) {
        pq->front = pq->rear = -1;
    } else {
        pq->front++;
    }
}

void enqueueFrontDoubleEndedQueue(struct DoubleEndedQueue* deq, int value) {
    if (isDoubleEndedQueueFull(deq)) {
        printf("Queue is full. Cannot insert element %d at the front\n", value);
        return;
    }
    if (isDoubleEndedQueueEmpty(deq)) {
        deq->front = deq->rear = 0;
    } else if (deq->front == 0) {
        deq->front = MAX_SIZE - 1;
    } else {
        deq->front--;
    }
    deq->arr[deq->front] = value;
    printf("Inserted %d at the front of the double-ended queue\n", value);
}

void enqueueRearDoubleEndedQueue(struct DoubleEndedQueue* deq, int value) {
    if (isDoubleEndedQueueFull(deq)) {
        printf("Queue is full. Cannot insert element %d at the rear\n", value);
        return;
    }
    if (isDoubleEndedQueueEmpty(deq)) {
        deq->front = deq->rear = 0;
    } else if (deq->rear == MAX_SIZE - 1) {
        deq->rear = 0;
    } else {
        deq->rear++;
    }
    deq->arr[deq->rear] = value;
    printf("Inserted %d at the rear of the double-ended queue\n", value);
}

void dequeueFrontDoubleEndedQueue(struct DoubleEndedQueue* deq) {
    if (isDoubleEndedQueueEmpty(deq)) {
        printf("Queue is empty. Cannot delete element from the front\n");
        return;
    }
    printf("Deleted %d from the front of the double-ended queue\n", deq->arr[deq->front]);
    if (deq->front == deq->rear) {
        deq->front = deq->rear = -1;
    } else if (deq->front == MAX_SIZE - 1) {
        deq->front = 0;
    } else {
        deq->front++;
    }
}

void dequeueRearDoubleEndedQueue(struct DoubleEndedQueue* deq) {
    if (isDoubleEndedQueueEmpty(deq)) {
        printf("Queue is empty. Cannot delete element from the rear\n");
        return;
    }
    printf("Deleted %d from the rear of the double-ended queue\n", deq->arr[deq->rear]);
    if (deq->front == deq->rear) {
        deq->front = deq->rear = -1;
    } else if (deq->rear == 0) {
        deq->rear = MAX_SIZE - 1;
    } else {
        deq->rear--;
    }
}

void displayCircularQueue(struct CircularQueue* cq) {
    if (isCircularQueueEmpty(cq)) {
        printf("Queue is empty\n");
        return;
    }
    int i = cq->front;
    do {
        printf("%d ", cq->arr[i]);
        i = (i + 1) % MAX_SIZE;
    } while (i != (cq->rear + 1) % MAX_SIZE);
    printf("\n");
}

void displayPriorityQueue(struct PriorityQueue* pq) {
    if (isPriorityQueueEmpty(pq)) {
        printf("Queue is empty\n");
        return;
    }
    for (int i = pq->front; i <= pq->rear; i++) {
        printf("%d ", pq->arr[i]);
    }
    printf("\n");
}

void displayDoubleEndedQueue(struct DoubleEndedQueue* deq) {
    if (isDoubleEndedQueueEmpty(deq)) {
        printf("Queue is empty\n");
        return;
    }
    int i = deq->front;
    do {
        printf("%d ", deq->arr[i]);
        i = (i + 1) % MAX_SIZE;
    } while (i != (deq->rear + 1) % MAX_SIZE);
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
