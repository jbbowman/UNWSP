#include <stdio.h>

typedef struct edge {
    char start;
    char end;
    int weight;
} edge;

void printEdge(edge myEdge) {
    printf("%c<-%d->%c", myEdge.start, myEdge.weight, myEdge.end);
}

edge buildEdge(char start, char end, int weight) {
    edge oneEdge;
    oneEdge.start = start;
    oneEdge.end = end;
    oneEdge.weight = weight;
    return oneEdge;
}

void printGraph(edge myGraph[], int size) {
    for (int i = 0; i < size; ++i) {
        printEdge(myGraph[i]);
        printf("\n");
}}

int main() {
    edge graph[100];
    int edgesAmt;

    printf("How many edges does the graph have? ->");
    scanf("%d", &edgesAmt);

    for (int i = 0; i < edgesAmt; ++i) {
        int weight;
        char start = i + 65, end = i + 66;

        printf("What is the weight of edge %d? ->", i + 1);
        scanf("%d", &weight);
        graph[i] = buildEdge(start, end, weight);
    }
    printGraph(graph, edgesAmt);
    return 0;
}

/*
void printVertex(edge myGraph[], int size, char c) {
    for (int i = 0; i < size; ++i) {
        if ((myGraph[i].start == c) || (myGraph[i].end = c)) {
            printEdge(myGraph[i]);
        }
        printf("\n");
}}
 */