#include <stdio.h>
#include <math.h>
#include <time.h>
#include <stdlib.h>

int newList[101];

// every other item in a list is put in a new list
void listSkip(int array[], int size) {
    for (int i = 0, j = 0; i < size; i += 2, ++j) {
        newList[j] = array[i];
    }
}

int main() {
    printf("This program prints every other item in an integer array\n");

    srand(time(NULL));
    int size = rand() % 100;  // size of the array is random
    int list[size];

    // each array item is assigned a random value
    for (int i = 0; i < size; ++i) {
        list[i] = rand() % 100;
    }

    listSkip(list, size); // call the listSkip function

    // print regular list
    printf("Every item in the array:\n");
    for (int i = 0; i < size; ++i) printf("%d ", list[i]);

    // print updated list
    printf("\n\nEvery other item in the array: \n");
    for (int i = 0; i < ceil(size/2.0); ++i) printf("%d ", newList[i]);

    return 0;
}