#include <stdio.h>
#include <graphics.h>

int main() {
        int gd = DETECT,gm;
        initgraph(&gd, &gm, NULL);

        int i;
        int x1 = 50, x2 = 100;

        for (i = 0; i < 3; ++i) {
                rectangle(x1, 50, x2, 100);
                rectangle(x1 + 50, 100, x2 + 50, 150);
                x1 += 100;
                x2 += 100;
        }

        delay(10000);
        closegraph();

        return 0;
}
