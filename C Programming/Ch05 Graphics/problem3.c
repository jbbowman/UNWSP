#include <stdio.h>
#include <graphics.h>

void triangle4(int x1, int y1, int right, int top, int xchange, int ychange) {
        int i;

        for (i = 0; i < 4; i++) {
                int x2 = x1 + right, y2 = y1;
                int x3 = x1 + top, y3 = y1 + right;
                line(x1, y1, x2, y2);
                line(x2, y2, x3, y3);
                line(x3, y3, x1, y1);

                x1 += xchange;
                y1 += ychange;
        }
}

int main() {
        int gd = DETECT,gm;
        initgraph(&gd, &gm, NULL);

        triangle4(50, 50, 50, 25, 25, 50);
        triangle4(50, 50, 50, 25, 50, 0);
        triangle4(350, 250, -50, -25, -25, -50);
        triangle4(350, 250, -50, -25, -50, 0);

        delay(10000);
        closegraph();

        return 0;
}
