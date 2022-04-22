#include <stdio.h>
#include <math.h>

int main()
{
    printf("This program asks for an angle measure between 0 and 360 and prints\n"
           "the angles sine, cosine, tangent, secant, cosecant, and cotangent\n");

    // gets a number from the user and stores it in variable num
    double num;
    printf("Please enter an angle between 0 and 360:");
    scanf("%lf", &num);

    // if the number is between 0 and 360, calculations are made and results are printed
    if (num >= 0 && num <= 360)
    {
        num = num * (M_PI / 180.0);
        double sine = sin(num);
        double cosine = cos(num);
        double tangent = tan(num);
        double secant = 1 / cos(num);
        double cosecant = 1 / sin(num);
        double cotangent = 1 / tan(num);

        printf("Results...\n"
               "\t Sine = %f\n"
               "\t Cosine = %f\n"
               "\t Tangent = %f\n"
               "\t Secant = %f\n"
               "\t Cosecant = %f\n"
               "\t Cotangent = %f\n",
               sine, cosine, tangent, secant, cosecant, cotangent);
    }
    else printf("That value is not between 0 and 360\n");

    printf("End of program");
    return 0;
}