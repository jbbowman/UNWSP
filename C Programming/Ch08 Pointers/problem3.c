#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main() {
    char book[20], bookInput[20];
    int chapters, chaptersInput, precChaptersCount = 0, follChaptersCount = 0;
    int found;
    FILE *data;
    data = fopen("bible.txt", "r");

    printf("Please enter a book and chapter ->");
    scanf("%s %d", &bookInput, &chaptersInput);

    for (int i = 0; i < 66; ++i) {
        fscanf(data, "%s", &book);
        fscanf(data, "%d", &chapters);
        if (strcmp(book, bookInput) != 0 && found != 1) {
            precChaptersCount += chapters;
        } else if (strcmp(book, bookInput) == 0) {
            precChaptersCount += chaptersInput - 1;
            follChaptersCount += chapters - chaptersInput;
            found = 1;
        } else if (strcmp(book, bookInput) != 0 && found == 1) {
            follChaptersCount += chapters;
        }
    }
    printf("%d chapters precede and %d chapters follow\n", precChaptersCount, follChaptersCount);

    fclose(data);
    printf("End of program.\n"); return 0;
}
