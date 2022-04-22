#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int list[100];

void bubblesort(int n) {
    int i;  // iterator 1
    int j;  // iterator 2

    for (i = 0; i < n - 1 ; ++i) {
        for (j = 0; j < n - 1; ++j) {
            int temp;  // temporary storage
            if (list[j] > list[j + 1]) {
                temp = list[j];
                list[j] = list[j + 1];
                list[j + 1] = temp;
            }}}}

int main () {
    int i;  // iterator
    int n = 1000;  // quantity of numbers
    srand(time(NULL));

    // randomize a list
    for (i = 0; i < n; ++i) {
        list[i] = rand() % 10001;   // random number between 0 and 10,000
    }

    // print the list
    printf("Randomized list:\n");
    for (i = 0; i < n; ++i) {
        printf("%4d ", list[i]);
    }

    bubblesort(n);

    // print the list again
    printf("\n\nBubble sorted list:\n");
    for (i = 0; i < n; ++i) {
        printf("%4d ", list[i]);
    }
    return 0;
}
