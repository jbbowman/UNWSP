#include <stdio.h>
#include <stdbool.h>
#include <math.h>

int main() {
    int num;

    printf("Please enter a number between 1 and 100,000 to see if it is prime->");
    scanf("%d", &num);

    // number must be between 1 and 100000
    if ((num >= 1) && (num <= 100000)) {
        int i = 2; bool composite;

        // loop checks for factors of a number between 2 and sqroot of itself
        while (i <= sqrt(num)) {
            // if the number divided by something between 2 and sqroot of itself, it is composite
            if (num % i == 0) {
                composite = true;
                break;}
            i++;
        }
        if (composite == false) printf("The number is prime");
        else printf("The number is composite");
    }
    else printf("Error: Did not input a number between 1 and 100,000");

    return 0;
}
