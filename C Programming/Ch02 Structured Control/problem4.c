#include <stdio.h>

int main()
{
    printf("This program asks for three decimal numbers and prints the largest of the three\n");

    int i;
    double nums[3];

    // user prompted to enter 3 numbers
    for (i = 0; i < 3; ++i)
    {
        printf("Enter number %i ->", i + 1);
        scanf("%lf", &nums[i]);
    }

    for (i = 1; i < 3; ++i) // loop occurs 2 times
    {
        // if 1st number is less than the 2nd number, the 2nd replaces the first; else: first remains
        // the same...; the first number in the array is then printed as the largest number
        if (nums[0] < nums[i]) nums[0] = nums[i];
    }
    printf("The largest number is %lf", nums[0]);

    return 0;
}
