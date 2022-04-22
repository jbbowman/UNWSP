#include <stdio.h>

int oddlist[500];

void odd(int length) {
    // i provides odd numbers; j counts number of loops
    for (int i = 1, j = 0; j < length; i += 2, ++j) {
        oddlist[j] = i;
    }
}

int main() {
    printf("This program finds a desired range of consecutive odd numbers beginning w/ 1\n");
    int num;

    printf("Please enter a number up to 500 ->");
    scanf("%d", &num);

    // numbers must be less than 500
    if (num > 500) {
        printf("That number is too large!");
        return -1;
    }

    odd(num);

    // prints contents of oddlist
    for (int i = 0; i < num; ++i) {
        printf("%d\n", oddlist[i]);
    }

    return 0;
}

