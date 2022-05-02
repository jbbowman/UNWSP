#include <stdio.h>

// the function will recursively and concurrently call itself, finding n * the factorial of n - 2 until n = 1
int dfact(int n) {
    if (n>=1) return n * dfact(n - 2);

    else return 1;
}

int main() {
    printf("This program calculates the double factorial of a number\n");

    int n;

    // user enters number less than 20
    printf("Enter a positive integer less than 20 ->");
    scanf("%d", &n);

    // catch invalid numbers
    if (n > 20 || n < 0) printf("Not a valid number.");

    // call dfact function
    else printf("The double factorial of %d = %ld", n, dfact(n));

    return 0;
}