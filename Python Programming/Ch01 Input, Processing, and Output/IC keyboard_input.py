'''
Developer: Jack Bowman
Program: keyboard_input
Date: 01/14/2022
'''
Name = input('Please input your name ') #Gets the name of the user
Age = float(input('Please input your age ')) #Gets the age of the user
Income = float(input('Please input your income $')) #Gets the income of the user
print(f'Your name is {Name}. You are {Age:.2f} years old, and you make ${Income:,.2f} a year.') #prints the outcome of the 3 variables
