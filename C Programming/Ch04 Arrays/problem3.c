#include <stdio.h>

int main() {
    int BT[8][8];
    int i1, i2;

    // initializing first two values of Bell's Triangle in order to compute the rest
    BT[0][0] = 1;
    BT[1][0] = 1;

    // loop finds value of current index by looking to the left and top left values of triangle
    for (i1 = 1; i1 < 8; ++i1) {
        for (i2 = 1; i2 < i1 + 1; ++i2) {

            BT[i1][i2] = BT[i1][i2 - 1] + BT[i1 - 1][i2 - 1];
            BT[i1 + 1][0] = BT[i1][i2];

        }
    }

    // prints the values stored in bell's triangle array
    for (i1 = 0; i1 < 8; ++i1) {
        for (i2 = 0; i2 < i1 + 1; ++i2) {
            printf("%d ", BT[i1][i2]);
        }
        printf("\n");
    }
}
