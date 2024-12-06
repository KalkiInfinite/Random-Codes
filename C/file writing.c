#include <stdio.h>
#include <stdlib.h>

struct student {
    char name[50];
    int roll_number;
};

int main() {
    struct student s[5];
    FILE *fp, *fp2;

    for (int i = 0; i < 5; i++) {
        printf("Enter name of student %d: ", i + 1);
        scanf("%s", s[i].name);
        printf("Enter roll number of student %d: ", i + 1);
        scanf("%d", &s[i].roll_number);
    }

    fp = fopen("info.txt", "w");
    if (fp == NULL) {
        printf("Error opening file 'info.txt'\n");
        return 1; 
    }

    for (int i = 0; i < 5; i++) {
        fprintf(fp, "Name: %s\nRoll Number: %d\n", s[i].name, s[i].roll_number);
    }
    fclose(fp);

    fp2 = fopen("backup.txt", "w");
    if (fp2 == NULL) {
        printf("Error opening file 'backup.txt'\n");
        return 1; s
    }

    fp = fopen("info.txt", "r");
    if (fp == NULL) {
        printf("Error reading file 'info.txt'\n");
        fclose(fp2);
        return 1;
    }

    char c;
    while ((c = fgetc(fp)) != EOF) {
        fputc(c, fp2);
    }

    fclose(fp);
    fclose(fp2);

    printf("Data has been successfully written to 'info.txt' and backed up in 'backup.txt'.\n");

    return 0;
}
