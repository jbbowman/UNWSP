#include <graphics.h>
#include <math.h>
#include <stdlib.h>

void tree(int x1, int y1, double theta, int dep, double length) {
    int x2, y2;
    double angle, angleAdjust;

    if (dep != 0) {
        // move
        x2 = x1 + length * cos(0.0174 * theta);
        y2 = y1 + length * sin(0.0174 * theta);

        // draw lines
        for (int i = 0; i < dep; ++i) {
            line(x1, y1, x2, y2);
        }

        // adjust angle of branches
        angleAdjust = 90 / (4 - 1.0);
        angle = theta - 90 / 2.0 - angleAdjust;

        // draw branches
        for (int i = 0; i < 4; ++i) {
            angle += angleAdjust;

            // call tree function again (depth and branch length decrease)
            tree(x2, y2, angle, dep - 1, length * 0.7);
        }}}

int main() {
    int gd = DETECT, gm;
    initgraph (&gd, &gm, NULL);

    tree(250, 400, 270, 5, 50);

    getch();
    closegraph();
}
