#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    printf("This program prints a random ASCII character between 32 and 126\n");

    // produces a seed for a series of random integers based on time elapsed since 1/1/1970
    srand(time(0));

    // produces random value between 32 and 126
    int num = rand() % (126 + 1 - 32) + 32;

    printf("Random character = %c\n", num);

    printf("End of program");
    return 0;
}