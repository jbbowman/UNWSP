#include <stdio.h>

int binsearch(int array[], int size, int num) {
    int mid, lower = 0, upper = size;

    // array is continually separated into binary nodes until num is found in respective leaf node
    for (mid = (lower + upper) / 2; lower <= upper; mid = (lower + upper) / 2) {
        if (array[mid] == num) return mid;  // num is found
        if (array[mid] > num) upper = mid - 1;  // num is in first binary node
        else lower = mid + 1;  // num is in second binary node
    }
    return -1;  // -1 is returned if num not in array
}

int main() {
    int num;
    int array[10] = {1, 2, 3, 9, 11, 13, 17, 25, 57, 90};

    printf("Enter number to search: ");
    scanf("%d", &num);

    // if num in array
    if (binsearch(array, 9, num) > -1)
        printf("The number is at position %d in the array.", binsearch(array, 9, num));

    // if num not in array
    else printf("The number entered is not in the list.");
}