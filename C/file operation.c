#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *fsring1, *fsring2, *ftemp;
    char ch, file1[50], file2[50], file3[50];

    printf("Enter name of the first file: ");
    scanf("%s", file1);
    printf("Enter name of the second file: ");
    scanf("%s", file2);
    printf("Enter name to store merged file: ");
    scanf("%s", file3);

    fsring1 = fopen(file1, "r");
    if (fsring1 == NULL) {
        perror("Error opening the first file");
        exit(EXIT_FAILURE);
    }

    fsring2 = fopen(file2, "r");
    if (fsring2 == NULL) {
        perror("Error opening the second file");
        fclose(fsring1); 
        exit(EXIT_FAILURE);
    }

    ftemp = fopen(file3, "w");
    if (ftemp == NULL) {
        perror("Error creating the merged file");
        fclose(fsring1);
        fclose(fsring2);
        exit(EXIT_FAILURE);
    }

    while ((ch = fgetc(fsring1)) != EOF) {
        fputc(ch, ftemp);
    }

    while ((ch = fgetc(fsring2)) != EOF) {
        fputc(ch, ftemp);
    }

    printf("Files '%s' and '%s' merged into '%s' successfully.\n", file1, file2, file3);

    fclose(fsring1);
    fclose(fsring2);
    fclose(ftemp);

    return 0;
}
