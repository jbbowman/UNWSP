#include <stdio.h>

int main() {

    int num;

    printf("        Multiplication Table\n");
    printf("---------------------------------------\n");

    for (int row = 1; row < 10; ++row) {
        for (int col = 1; col < 10; ++col) {
            num = row * col;
            printf("%4d", num);
        }
        printf("\n");
    }
    printf("---------------------------------------\n");

    return 0;
}