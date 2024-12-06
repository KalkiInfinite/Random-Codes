#include <stdio.h>
#include <stdlib.h>

struct NODE {
    int data;
    struct NODE *right;
    struct NODE *left;
};

struct NODE* root = NULL;

// Function to insert a node into the binary tree
struct NODE* insert(struct NODE* node, int value) {
    if (node == NULL) {
        struct NODE* newNode = (struct NODE*)malloc(sizeof(struct NODE));
        newNode->data = value;
        newNode->left = NULL;
        newNode->right = NULL;
        if (root == NULL) {
            root = newNode;
        }
        return newNode;
    } else if (value <= node->data) {
        node->left = insert(node->left, value);
    } else {
        node->right = insert(node->right, value);
    }
    return node;
}

// In-order traversal (left -> root -> right)
void traverse_inorder(struct NODE* node) {
    if (node == NULL) {
        return;
    }
    traverse_inorder(node->left);
    printf(" %d", node->data);
    traverse_inorder(node->right);
}

// Pre-order traversal (root -> left -> right)
void traverse_preorder(struct NODE* node) {
    if (node == NULL) {
        return;
    }
    printf(" %d", node->data);
    traverse_preorder(node->left);
    traverse_preorder(node->right);
}

// Post-order traversal (left -> right -> root)
void traverse_postorder(struct NODE* node) {
    if (node == NULL) {
        return;
    }
    traverse_postorder(node->left);
    traverse_postorder(node->right);
    printf(" %d", node->data);
}

int main() {
    int choice, value;

    printf("Binary Tree Operations:\n");
    printf("1. Create/Insert\n");
    printf("2. In-order Traversal\n");
    printf("3. Pre-order Traversal\n");
    printf("4. Post-order Traversal\n");
    printf("5. Exit\n");

    while (1) {
        printf("\nEnter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter value to insert: ");
                scanf("%d", &value);
                insert(root, value);
                break;

            case 2:
                printf("In-order Traversal: ");
                traverse_inorder(root);
                printf("\n");
                break;

            case 3:
                printf("Pre-order Traversal: ");
                traverse_preorder(root);
                printf("\n");
                break;

            case 4:
                printf("Post-order Traversal: ");
                traverse_postorder(root);
                printf("\n");
                break;

            case 5:
                printf("Exiting the program.\n");
                return 0;

            default:
                printf("Invalid choice! Please try again.\n");
        }
    }

    return 0;
}
