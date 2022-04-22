#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    char input;
    srand(time(0));

    while (0 == 0) {
        printf("Would like like to roll the 2 dice? (y or n) ->");
        scanf("%s", &input);

        // if "y" is answered, 2 random values between 1 and 6 are found
        if (input == 'y') {
            printf("Dice 1 = %d\n", rand() % 6 + 1);
            printf("Dice 2 = %d\n", rand() % 6 + 1);
        }

        // "n" breaks infinite while loop
        else if (input == 'n') break;

        // catches unrecognized input
        else printf("Unrecognized input; Please enter y or n...\n");
    }
    printf("End of program");
    return 0;
}