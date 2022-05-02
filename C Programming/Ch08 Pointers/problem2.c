#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

// prints the maze
void Maze(const char *p) {
    for (int i = 0; i < 20; ++i) {
        for (int j = 0; j < 20; ++j) {
            printf("%c", *p);
            p += 1;
        } printf("\n");
    } printf("\n");
}

int main() {
    char maze[20][20], *pMaze = &maze[0][0], temp;  // stores maze and pointer to first value
    int dir, x, y;  // stores temp direction of arrow
    srand(time(NULL));  // seeds rand()

    // prints random arrows in each maze position
    for (int i = 0; i < 400; ++i) {
        dir = rand() % 4;
        if (dir == 0) *pMaze = '^';
        else if (dir == 1) *pMaze = 'V';
        else if (dir == 2) *pMaze = '>';
        else if (dir == 3) *pMaze = '<';
        pMaze += 1;
    }
    Maze(&maze[0][0]);  // prints maze

    printf("Please select any point on the boundary of the grid (x, y)->");
    scanf("%d, %d", &x, &y);  // user enters a position
    pMaze = &maze[x-1][y-1];

    // moves based on direction of arrow and puts X in occupied spot
    while (*pMaze == '^' || *pMaze == 'V' || *pMaze == '>' || *pMaze == '<') {
        temp = *pMaze;
        *pMaze = 'X';
        Maze(&maze[0][0]);
        if (temp == '^') pMaze -= 20;
        else if (temp == 'V') pMaze += 20;
        else if (temp == '>') pMaze += 1;
        else if (temp == '<') pMaze -= 1;
        sleep(1);
    }
    printf("End of program."); return 0;
}