#include <stdio.h>
#include <graphics.h>

void square(int x, int y, int l) {
        rectangle(x, y, x + l, y + l);
}

int main() {
        int gd = DETECT,gm;
        initgraph(&gd, &gm, NULL);

        // eyes
        for (int i = 100; i < 250; i += 10) {
                square(200, i, 10);
                square(400, i, 10);
        }

        // mouth
        for (int i = 100; i < 500; i += 10) {
                square(i, 400, 10);
        }

        // ends of mouth
        for (int i = 300; i < 400; i += 10) {
                square(100, i, 10);
                square(490, i, 10);
        }

        delay(10000);
        closegraph();

        return 0;
}
