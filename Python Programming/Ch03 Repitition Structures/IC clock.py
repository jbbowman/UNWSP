'''
Developer: Jack Bowman
Program: clock
Date: 01/28/2022
'''

import time  # imports time module

try:
    x = int(input('Please enter the number of minutes: '))  # gets desired minutes to count to from user
    for minutes in range(0, x):  # loop for desired range of minutes
        for seconds in range(0, 60):  # loop for 60 seconds in a minute
            print(f'\rTime = {minutes} minutes and {seconds} seconds', end='')
            time.sleep(.1)
            # Display minutes and seconds

except Exception:
    print('Input not recognized')