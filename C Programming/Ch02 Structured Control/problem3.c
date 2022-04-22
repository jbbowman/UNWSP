#include <stdio.h>
#include <math.h>
int main()
{
    printf("This program is a quadratic formula calculator\n");

    double n[3], disc, ans1, ans2;
    char l[3] = "abc";
    int i;

    // gets variables a, b, and c from user
    for (i = 0; i < 3; ++i)
    {
        printf("Enter coefficient %c ->", l[i]);
        scanf("%lf", &n[i]);
    }

    // calculates discriminant of quadratic
    disc = n[1] * n[1] - 4 * n[0] * n[2];

    if (disc > 0) // if discriminant > 0, two real nums displayed
    {
        ans1 = (-n[1] + sqrt(disc)) / (2 * n[0]);
        ans2 = (-n[1] - sqrt(disc)) / (2 * n[0]);
        printf("The solutions are: %lf %lf", ans1, ans2);
    }
    else if (disc == 0) // if discriminant = 0, one real num is displayed
    {
        ans1 = -n[1] / (2 * n[0]);
        printf("The solution is: %lf", ans1);
    }
    else printf("Solution(s) result in non-real numbers"); // non-real numbers not calculated

    return 0;
}
