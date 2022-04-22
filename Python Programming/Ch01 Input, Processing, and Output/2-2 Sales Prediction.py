'''
Developer: Jack Bowman
Program: 2-2 Sales Prediction
Date: 01/17/2022
'''

projectedTotalSales = input('What is the projected amount of total sales? $')
# gets projected total sales from user
percentAnnualProfit = 0.23
# percent annual profit variable

try:
    profit = float(projectedTotalSales) * percentAnnualProfit
    print(f'Your projected profit is ${profit:,.2f}')
# multiplies projected total sales by percent annual profit and prints the result
except ValueError:
    print("The projected amount of total sales you entered is formatted incorrectly. Please enter the value using"
          " digits and don't use commas.")
# the try-except statement above informs the user if their input is not a floating point
