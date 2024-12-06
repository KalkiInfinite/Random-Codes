#include <stdio.h>
#include <string.h>

struct player {
    char name[50];
    int total_matches;
    int best_bowling;
};

void insert_player(struct player players[], int size) {
    for (int i = 0; i < size; i++) {
        printf("Enter player %d details:\n", i + 1);
        printf("Name: ");
        scanf("%s", players[i].name);
        printf("Total matches played: ");
        scanf("%d", &players[i].total_matches);
        printf("Best bowling figure (wickets): ");
        scanf("%d", &players[i].best_bowling);
    }
}

int compare(const void *a, const void *b) {
    int l = ((struct player *)a)->best_bowling;
    int r = ((struct player *)b)->best_bowling;
    return (r - l);
}

void display_players(struct player players[], int size) {
    printf("Name\t\tTotal Matches\tBest Bowling Figure\n");
    for (int i = 0; i < size; i++) {
        printf("%s\t\t%d\t\t%d\n", players[i].name, players[i].total_matches, players[i].best_bowling);
    }
}

int delete_player(struct player players[], int size, char name[]) {
    for (int i = 0; i < size; i++) {
        if (strcmp(players[i].name, name) == 0) {
            for (int j = i; j < size - 1; j++) {
                players[j] = players[j + 1];
            }
            printf("Player %s deleted successfully.\n", name);
            return size - 1;
        }
    }
    printf("Player %s not found.\n", name);
    return size;
}

void search_player(struct player players[], int size, char name[]) {
    for (int i = 0; i < size; i++) {
        if (strcmp(players[i].name, name) == 0) {
            printf("Player found:\n");
            printf("Name: %s\n", players[i].name);
            printf("Total matches played: %d\n", players[i].total_matches);
            printf("Best bowling figure: %d\n", players[i].best_bowling);
            return;
        }
    }
    printf("Player %s not found.\n", name);
}

int main() {
    struct player players[5];
    int size = 5;

    insert_player(players, size);

    qsort(players, size, sizeof(struct player), compare);

    printf("\nPlayers sorted by best bowling figures:\n");
    display_players(players, size);

    char name[50];
    printf("\nEnter player name to delete: ");
    scanf("%s", name);
    size = delete_player(players, size, name);

    printf("\nUpdated player list:\n");
    display_players(players, size);

    printf("\nEnter player name to search: ");
    scanf("%s", name);
    search_player(players, size, name);

    return 0;
}
