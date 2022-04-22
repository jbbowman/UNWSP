#include <stdio.h>

int main()
{
    printf("This program asks for two boolean values and prints out the expressions\n"
           "of x OR y, x AND y, x NAND y, x IMPLIES y, x IFF y, x XOR y\n");

    int x, y;

    // gets two boolean values from user
    printf("Enter boolean value x (true=1 or false=0):");
    scanf("%i", &x);
    printf("Enter boolean value y (true=1 or false=0):");
    scanf("%i", &y);

    // prints results of each logic expression
    printf("Results if x = %i and y = %i...\n", x, y);
    printf("\tx OR y = %i\n", x || y);
    printf("\tx AND y = %i\n", x && y);
    printf("\tx NAND y = %i\n", !(x && y));
    printf("\tx IMPLIES y = %i\n", !(x || y));
    printf("\tx IFF y = %i\n", x == y);
    printf("\tx XOR y = %i\n", x ^ y);

    printf("End of program");
    return 0;
}