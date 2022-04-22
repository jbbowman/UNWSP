'''
Developer: Jack Bowman
Program: 3-8 Hot Dog Calculator
Date: 01/24/2022
'''

import math  # imports math module to use its ceil function, which rounds numbers up

hotDogCount = 10
bunCount = 8
# variables above specify the number of hot dogs and buns in each package

try:
    attendance = int(input('How many people will be attending the cookout? '))
    servingSize = float(input('How many hot dogs will each individual have? '))
    totalServings = attendance * servingSize
    # collects number of people attending the cookout and the number of hot dogs each person will be given

    hotDogPackages = math.ceil(totalServings / hotDogCount)
    bunPackages = math.ceil(totalServings / bunCount)
    # calculates hot dog and bun packages needed

    hotDogLeftovers = hotDogCount - (totalServings % hotDogCount)
    bunLeftovers = bunCount - (totalServings % bunCount)
    # calculates hot dogs and buns left over

    print(f'You will need {hotDogPackages:,.1f} package(s) of hot dogs '
          f'and {bunPackages:,.1f} package(s) of buns')
    print(f'You will have {hotDogLeftovers:,.1f} hot dog(s) left over '
          f'and {bunLeftovers:,.1f} bun(s) leftover')
    # displays packages needed and resulting leftovers

except Exception:
    print('Something went wrong!')
# captures unrecognized inputs
