'''
Developer: Jack Bowman
Program: 4-7 Pennies for Pay
Date: 01/28/2022
'''

try:
    totalDays = int(input('How many days should your salary double beginning with 1 penny? '))
    # gets number of days to double the users salary
    initialValue = 1/100
    # gets initial amount

    print(f'If you started with a salary of 1 penny and it doubled everyday for {totalDays} days...')

    for day in range(1, totalDays + 1):  # loops statements below the number of times the user specified earlier
        print(f' After {day} day(s), your salary would equal ${initialValue:,.2f}')
        initialValue *= 2  # doubles initial value
        # prints doubled value for relative day
    print(f'Your final salary would be ${initialValue / 2:,.2f}')
    # reprints final value
except Exception:
    print('Unrecognized input.')
# traps unrecognized inputs
