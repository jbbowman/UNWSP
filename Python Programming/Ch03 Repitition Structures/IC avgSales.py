'''
Developer: Jack Bowman
Program: IC avgSales
Date: 01/26/2022
'''

numberSales = totalSales = averageSales = 0
# creates variables for number of sales, total sales, and average sales

while True:  # creates loop for entering multiple sales
    try:
        sale = float(input('Enter a sale made or type "0" to exit the program $'))
        if sale > 0:
            numberSales += 1
            totalSales += sale
            averageSales = totalSales/numberSales
            print(f'The total of your {numberSales} sale(s) is ${totalSales:,.2f} and your average is ${averageSales:,.2f}')
            # gets a sales number from the user and prints the number of sales, total sales, and average sales
        else:
            print('You have exited the program')
            break
            # exits the program if user enters 0
    except Exception:
        print('Not a recognized input. Try again...')
    # traps errors
