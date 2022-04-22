#include <stdio.h>
#include <graphics.h>

int main() {
        int gd = DETECT,gm;
        initgraph(&gd, &gm, NULL);

        // creates lines clockwise for star pattern
        int x1, x2;
        for (x1 = 0, x2 = 100; x1 < 101; x1 += 50, x2 -= 50) {
                line(x1, 0, x2, 100);
        }

        line(0, 50, 100, 50);


        delay(10000);
        closegraph();

        return 0;
}
