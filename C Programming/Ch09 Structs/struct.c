#include <stdio.h>

typedef struct cat {
    char name[15];
    char breed[15];
    char fur[15];
    double weight;
    int age;
    char litterbox[15];
    char toy[15];
    char mood[15];
    char food[15];
} cat;

void printInfo (cat myCat) {
    printf("\n%s's Characteristics...\n"
           "Breed: %s\n"
           "Fur: %s\n"
           "Weight: %d\n"
           "Age: %d\n"
           "Litterbox: %s\n"
           "Toy: %s\n"
           "Mood: %s\n"
           "Food: %s\n",
           myCat.name, myCat.breed, myCat.fur, myCat.weight, myCat.age,
           myCat.litterbox, myCat.toy, myCat.mood, myCat.food);
    printf("\n");
}

cat getCatInfo() {
    cat myCat;
    char phrase[25] = "What is the cat's";

    printf("%s name?", phrase); scanf("%s", &myCat.name);
    printf("%s breed?", phrase); scanf("%s", &myCat.breed);
    printf("%s fur?", phrase); scanf("%s", &myCat.fur);
    printf("%s weight?", phrase); scanf("%d", &myCat.weight);
    printf("%s age?", phrase); scanf("%d", &myCat.age);
    printf("%s litterbox?", phrase); scanf("%s", &myCat.litterbox);
    printf("%s toy?", phrase); scanf("%s", &myCat.toy);
    printf("%s mood?", phrase); scanf("%s", &myCat.mood);
    printf("%s food?", phrase); scanf("%s", &myCat.food);

    return myCat;
}

int main() {
    cat myCat;

    myCat = getCatInfo();
    printInfo(myCat);

    return 0;
}