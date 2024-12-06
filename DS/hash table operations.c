#include <stdio.h>
#include <stdlib.h>

struct HashChair {
    int key;
};

int hashCode(int size, int key) {
    return key % size;
}

void insert(struct HashChair **hashTable, int size, int key) {
    struct HashChair *newChair = (struct HashChair *)malloc(sizeof(struct HashChair));
    newChair->key = key;

    int hashIndex = hashCode(size, key);

    while (hashTable[hashIndex] != NULL) {
        ++hashIndex;
        hashIndex %= size;
    }

    hashTable[hashIndex] = newChair;
    printf("%d successfully added to hash table\n\n", key);
}

void display(struct HashChair **hashTable, int size) {
    for (int i = 0; i < size; i++) {
        if (hashTable[i] != NULL) {
            printf("Index %d: Key %d\n", i, hashTable[i]->key);
        } else {
            printf("Index %d: Empty\n", i);
        }
    }
    printf("\n");
}

int main() {
    int size;

    printf("Enter hash table size: ");
    scanf("%d", &size);
    printf("\n");

    struct HashChair **hashTable = (struct HashChair **)malloc(size * sizeof(struct HashChair *));
    for (int i = 0; i < size; i++) {
        hashTable[i] = NULL;
    }

    int choice;
    while (1) {
        printf("0: EXIT\n1: INSERT\n2: DISPLAY\n\nEnter choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 0:
                printf("Program successfully terminated.\n");
        
                for (int i = 0; i < size; i++) {
                    if (hashTable[i] != NULL) {
                        free(hashTable[i]);
                    }
                }
                free(hashTable);
                return 0;

            case 1: {
                int key;
                printf("Enter key: ");
                scanf("%d", &key);
                insert(hashTable, size, key);
                break;
            }

            case 2:
                display(hashTable, size);
                break;

            default:
                printf("Error: Invalid choice. Try again.\n");
        }
    }

    return 0;
}
