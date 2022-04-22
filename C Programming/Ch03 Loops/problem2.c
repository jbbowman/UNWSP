#include <stdio.h>
#include <math.h>

int main() {
    double num; int list[20], i = 0;

    printf("Please enter a number between 1 and 100,000 to see its prime decomposition ->");
    scanf("%lf", &num);

    if (num >= 1 && num <= 100000) {
        // Loop that continues until num = 1
        while (num != 1) {
            // Loop begins at 2 and tests all possibilities until prime factor is found and put in list
            for (int x = 2; x <= num; x++) {
                num = num / x;

                // if num is a whole number, the loop ends
                if (ceil(num) == num) {
                    list[i] = x;
                    break;
                }
                // num goes back to original value and for loop repeats
                else num = num * x;
            }
            printf("Number %i in the decomposition is %i\n", i + 1, list[i]);
            i++;
        }
    }
    else printf("Error: Number not between 1 and 100,000");

    return 0;
}
