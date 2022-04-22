'''
Developer: Jack Bowman
Program: 2-9 Temperature Converter
Date: 01/17/2022
'''

try:
    temp = float(input('What is the temperature? (Only enter an integer or floating point value): '))
    # gets the temperature from the user
    unit = input('Is this in (C)elsius or (F)ahrenheit? ').lower()
    # verifies whether temperature is in celsius or fahrenheit

    if unit == 'c' or unit == 'celsius':
        print(f'The temperature in Fahrenheit is {9/5 * temp + 32:,.1f} degrees')
    # converts celsius to fahrenheit
    elif unit == 'f' or unit == 'fahrenheit':
        print(f'The temperature in Celsius is {(temp - 32) * 5/9:,.1f} degrees')
    # converts fahrenheit to celsius
    else:
        print('Unit not recognized')
    # prints that the unit for temperature inputted is not recognized

except Exception:
    print('Something went wrong!')
# captures errors
