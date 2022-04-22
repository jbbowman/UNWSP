#include <stdio.h>
#include <math.h>

int main()
{
    printf("This program asks for two decimal numbers and prints their\n"
           "sum, average, difference, product, quotient, and exponentiation...\n");

    // get input
    float num1, num2;
    printf("Please enter the first decimal number:");
    scanf("%f", &num1);
    printf("Please enter the second decimal number:");
    scanf("%f", &num2);

    // calculations
    float sum = num1 + num2;
    float avg = (num1 + num2) / 2;
    float diff = num1 - num2;
    float product = num1 * num2;
    float quotient = num1 / num2;
    float exp = powf(num1, num2);

    // print results
    printf("Results...\n");
    printf("\tSum = %f\n", sum);
    printf("\tAverage = %f\n", avg);
    printf("\tDifference = %f\n", diff);
    printf("\tProduct = %f\n", product);
    printf("\tQuotient = %f\n", quotient);
    printf("\tExponentiation = %f\n", exp);

    printf("End of program");
    return 0;
}