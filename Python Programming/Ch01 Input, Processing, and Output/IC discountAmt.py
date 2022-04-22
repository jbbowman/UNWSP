'''
Developer: Jack Bowman
Program: discountAmt
Date: 01/14/2022
'''
price = float(input('Please input the price of the item $')) #price of item
discountRate = float(input('Please input the discount rate as a decimal ')) #discount rate
discountAmt = price * discountRate #amount discounted from order
total = price - discountAmt #order total
print(f'Your total after the discount is ${total:,.2f}') #prints the order total
