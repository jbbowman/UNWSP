#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char menu[] = "Menu\n"
                  "print.........Print the array of numbers (|x| = selected)\n"
                  "move..........Select a different number\n"
                  "change........Change the value of the selected number\n"
                  "help..........Display Menu again\n"
                  "quit..........Quit the program\n";

    srand(time(NULL));
    char input[10];  // stores user input
    int num[20];  // stores an array of random numbers
    int *pNum = &num[0];  // stores a pointer to the first item in the array
    int pointTo = 0;  // stores where to point to in the array
    int numSize = sizeof(num)/sizeof(num[0]);  // stores size of array

    // fills array with random numbers
    for (int i = 0; i < numSize; ++i) {
        num[i] = rand() % 10;
    }

    // prints the menu
    printf("%s", menu);

    while (0 == 0) {
        printf("\nPlease enter a command ->");
        scanf("%6s", &input);

        // prints all numbers in the array, including selected value
        if (strcmp(input, "print") == 0) {
            for (int i = 0; i < numSize; ++i) {
                if (i != pointTo) printf("%d ", *(pNum + i));
                else printf("|%d| ", *(pNum + pointTo));
            }
        }

        // changes selection
        else if (strcmp(input, "move") == 0) {
            int temp;
            printf("Please enter how many spaces to move ->");
            scanf("%d", &temp);
            pointTo += temp % 10;
            printf("Selection successfully changed");
        }

        // changes selected number
        else if (strcmp(input, "change") == 0) {
            printf("Please enter an integer to replace the selected number ->");
            scanf("%d", &*(pNum + pointTo));
            printf("Number successfully changed.");
        }

        else if (strcmp(input, "help") == 0) printf("%s", menu);
        else if (strcmp(input, "quit") == 0) break;
        else printf("Unrecognized command.");
    }
    printf("End of program.");
    return 0;
}