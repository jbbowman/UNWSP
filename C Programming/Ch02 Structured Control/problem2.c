#include <stdio.h>

int main()
{
    double temp, hum;
    for (int i = 1; i < 3; ++i)
    {
        printf("Please enter the temperature in degrees fahrenheit for area %d ->", i);
        scanf("%lf", &temp);

        printf("Please enter humidity in percent for area %d ->", i);
        scanf("%lf", &hum);

        if ((temp < 2) && (hum > 90))
        {
            printf("The plane needs to be deiced\n");
            break;
        }
    }
    return 0;
}
