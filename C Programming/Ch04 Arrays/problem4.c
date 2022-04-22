#include <stdio.h>
int main () {
    int m; //the number to partition

    printf("Enter a number between 1 and 50 to see how many partitions it has ->");
    scanf("%d", &m);

    int p[m];  //the summands in the partition
    int k = 0; //the summand we are working on
    p[k] = m;  //the first summand is m
    int sum = 0;  //the current sum of the summands
    int totPart = 0;  //the total number of partitions

    while (m > 0 && m < 51) {

        //print out the current analyzed summands
        sum = 0;
        for (int i = 0; i<m; i++)
        {
            sum += p[i];
        }
        totPart++;

        //work through remaining summands
        int rem_val = 0;
        while (k >= 0 && p[k] == 1)
        {
            rem_val += p[k];
            k--;
        }

        if (k < 0) {break;}

        //subtract one from summand and add one to remaining value
        p[k]--;
        rem_val++;
        // work through new reduced summand
        while (rem_val > p[k])
        {
            p[k+1] = p[k];
            rem_val = rem_val - p[k];
            k++;
        }

        // update new summand
        p[k+1] = rem_val;
        k++;
    }
    if (m > 0 && m < 51) printf ("There are %d partitions of %d.", totPart, m);
    else printf("That number is not within the specified range.");
}
