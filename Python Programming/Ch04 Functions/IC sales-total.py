# Developer: Jack Bowman
# Program: sales_total in-class
# Date: 02/07/2022

SALES_TAX = 1.07
subtotal = 0

def main():
    while True:
        try:
            global subtotal
            userInput = input('Please enter the price of an item or type done to checkout: $')
            if userInput == 'done':
                total = tax(subtotal)
                print(f'Your subtotal is ${subtotal:,.2f}, and your total after a {(SALES_TAX - 1) * 100:,.2f}% tax is ${total:,.2f}')
                break
            else:
                subtotal += float(userInput)
        except:
            print('Unrecognized command. Please try again or type done to checkout')
def tax(val):
    total = val * SALES_TAX
    return total

if __name__ == '__main__':
    main()