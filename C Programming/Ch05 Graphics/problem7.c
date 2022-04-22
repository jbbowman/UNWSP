#include <stdio.h>
#include <graphics.h>

int main() {
        int gd = DETECT,gm;
        initgraph(&gd, &gm, NULL);

        bar3d(200, 200, 300, 300, 50, 1);

        delay(10000);
        closegraph();

        return 0;
}
