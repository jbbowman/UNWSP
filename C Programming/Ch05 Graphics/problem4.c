#include <stdio.h>
#include <graphics.h>

void snowman(int topx, int topy,int  topr) {
        circle(topx, topy, topr);
        floodfill(topx, topy, WHITE);

        topr += 25;
        circle(topx, topy += topr + 25, topr);
        floodfill(topx, topy, WHITE);

        topr += 25;
        circle(topx, topy += topr + 50, topr);
        floodfill(topx, topy, WHITE);
}

void triangle(int x1, int y1, int x2, int y2, int x3, int y3) {
        line(x1, y1, x2, y2);
        line(x2, y2, x3, y3);
        line(x3, y3, x1, y1);
}

int main() {
        int gd = DETECT,gm;
        initgraph(&gd, &gm, NULL);

        // body
        snowman(300, 100, 25);
        setcolor(BLACK);

        // left eye
        circle(290, 95, 4);
        floodfill(290, 95, BLACK);

        // right eye
        circle(310, 95, 4);
        floodfill(310, 95, BLACK);

        // nose
        triangle(300, 100, 300, 105, 310, 103);

        // mouth (ellipse and arc weren't functioning properly)
        line(290, 110, 310, 110);

        // buttons
        for (int i = 150; i < 201; i += 25) {
                circle(300, i, 4);
        }

        // hat
        setcolor(WHITE);
        rectangle(275, 75, 325, 25);
        rectangle(250, 75, 350, 80);
        floodfill(300, 70, WHITE);
        floodfill(345, 78, WHITE);
        floodfill(255, 78, WHITE);

        delay(10000);
        closegraph();

        return 0;
}
