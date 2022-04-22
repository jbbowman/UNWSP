'''
Developer: Jack Bowman
Program: 3-16 February Days
Date: 01/24/2022
'''

try:
    year = int(input('What year is it? '))

    if year % 100 == 0:
        if year % 400 == 0:
            print('It is a leap year! There are 29 days in february.')
    elif year % 4 == 0:
        print('It is a leap year! There are 29 days in february.')
    else:
        print('It is not a leap year. There are only 28 days in february')

except Exception:
    print('Something went wrong!')
# captures unrecognized inputs
