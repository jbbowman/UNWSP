'''
Developer: Jack Bowman
Program: 2-4 Total Purchase
Date: 01/17/2022
'''

items = 0  # items in user's cart
subtotal = 0  # users total before tax
salesTax = .07  # tax rate

while True:  # establishes loop so multiple items can be entered
    itemPrice = input(f'Please enter the price of item {items + 1} or type "done" to checkout $').lower()
    # gets the price of the item from the user
    try:
        subtotal += float(itemPrice)
        items += 1
        print(f'Your running total is ${subtotal:,.2f}.')
    # if the user enters an integer or floating point, the number will be added to the subtotal
    except Exception:
        if itemPrice == 'done':
            total = subtotal * (1 + salesTax)
            print(f'The total of your {items} item(s) after tax is ${total:,.2f}')
            break
    # if the user enters "done," the total after tax will be given and the loop will break
        else:
            print('Not a recognized input. Please try again.')
    # if the user's entry is not recognized, the message above will be displayed
