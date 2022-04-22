#include <stdio.h>
#include <graphics.h>

void triangle(int x1, int y1, int x2, int y2, int x3, int y3) {
        line(x1, y1, x2, y2);
        line(x2, y2, x3, y3);
        line(x3, y3, x1, y1);
}

int main() {
        int gd = DETECT,gm;
        initgraph(&gd, &gm, NULL);

        // house body
        rectangle(200, 200, 350, 350);

        // roof
        triangle(150, 200, 400, 200, 275, 100);

        // door
        rectangle(260, 350, 290, 275);
        circle(282, 300, 2);

        delay(10000);
        closegraph();

        return 0;
}
