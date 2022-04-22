'''
Developer: Jack Bowman
Program: 2-14 Compound Interest
Date: 01/17/2022
'''

try:
    principalAmount = float(input('What is is the principal amount? '))
    interestRate = float(input('What is the annual interest rate? '))
    numberPerYear = float(input('What is the number of times per year that the interest is compounded? '))
    numberOfYears = int(input('How many years will this money accrue interest? '))
    # collects variables needed to calculate compound interest

    amount = principalAmount * (1 + interestRate / numberPerYear) ** (numberPerYear * numberOfYears)
    print(f'After {numberOfYears:,.0f} years, the account will have ${amount:,.2f}')
    # calculates compound interest and prints results
except Exception:
    print('Something went wrong!')
# captures errors
