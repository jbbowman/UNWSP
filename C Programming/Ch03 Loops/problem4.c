#include <stdio.h>
#include <math.h>

int main() {
    double num = 0;

    for (int i = 1; i < 1000000; ++i) {
       num += (1 / (pow(i, 3)));
    }
    printf("The infinite sum of 1/1^3 + 1/2^3 + 1/3^3 ... is approximately %.10lf", num);

    return 0;
}
