#include <stdio.h>

int main() {

    double sphere[50][3];
    int sphereAmt;
    int i1, i2;

    printf("This program stores the radius, volume, and surface area of up to 50 spheres\n");

    printf("How many spheres do you have to input? ->");
    scanf("%i", &sphereAmt);

    if (sphereAmt < 51 && sphereAmt > 0) {

        // stores sphere's radius, volume, and surface area in respective index
        for (i1 = 0; i1 < sphereAmt; ++i1) {
            printf("Please input sphere %i's radius ->", i1 + 1);
            scanf("%lf", &sphere[i1][0]);

            printf("Please input sphere %i's volume ->", i1 + 1);
            scanf("%lf", &sphere[i1][1]);

            printf("Please input sphere %i's surface area ->", i1 + 1);
            scanf("%lf", &sphere[i1][2]);
        }

        // prints table showing all spheres inputted
        printf("\t\tRadius Volume Surface\n");
        for (i1 = 0; i1 < sphereAmt; ++i1) {
            printf("Sphere %i:   ", i1 + 1);
            for (i2 = 0; i2 < 3; ++i2) {
                printf("%.4lf ", sphere[i1][i2]);
            }
            printf("\n");
        }
    }

    else printf("That number is not in the valid range\n");

    printf("End of program");
    return 0;
}