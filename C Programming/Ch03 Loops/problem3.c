#include <stdio.h>

int main() {
    char string[50] = "                                                  ";
    int v = 0, c = 0;
    char dummy, vowels[5] = "aeiou", consonants[21] = "bcdfghjklmnpqrstvwxyz";

    printf("Please enter a string up to 50 characters (use underscores for whitespace) ->");
    scanf("%50s%c", &string, &dummy);

    // loops through characters in user input
    for (int i1 = 0; i1 < 50; ++i1) {
        // loops through vowels to find matches
        for (int i2 = 0; i2 < 5; ++i2) {
            if (string[i1] == vowels[i2]) v++;
        }
        // loops through consonants to find matches
        for (int i2 = 0; i2 < 21; ++i2) {
            if (string[i1] == consonants[i2]) c++;
        }
    }
    printf("There is/are %i vowel(s) and %i consonant(s)", v, c);

    return 0;
}
