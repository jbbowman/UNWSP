#include <stdio.h>
#include <graphics.h>

int main() {
        int gd = DETECT,gm;
        initgraph(&gd, &gm, NULL);

        // wheels
        circle(100, 300, 50);
        circle(350, 300, 50);

        // steering column
        line(100, 300, 150, 150);

        // handle bars
        line(150, 150, 200, 150);

        // structure
        line(125, 225, 225, 300);
        line(225, 300, 350, 300);
        line(300, 190, 225, 300);
        line(275, 225, 350, 300);
        line(275, 225, 125, 225);

        // seat
        line(275, 190, 325, 190);

        delay(10000);
        closegraph();

        return 0;
}
