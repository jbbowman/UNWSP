#include <stdio.h>
int main() {
    int product;
    float quantity;
    double total = 0;

    // gets product number and quantity from user
    printf("Please enter a product number->");
    scanf("%i", &product);
    printf("Please enter the quantity->");
    scanf("%f", &quantity);

    // case exists for each product number and its respective price.
    // price is multiplied by quantity in each case
    switch(product)
    {
        case 1:
            total = quantity * 2.98;
            break;
        case 2:
            total = quantity * 4.5;
            break;
        case 3:
            total = quantity * 9.98;
            break;
        case 4:
            total = quantity * 4.49;
            break;
        case 5:
            total = quantity * 6.87;
            break;
        default:
            printf("That product does not exist\n");
    }
    // displays total price to user
    printf("The total cost is $%.2f", total);

    return 0;
}