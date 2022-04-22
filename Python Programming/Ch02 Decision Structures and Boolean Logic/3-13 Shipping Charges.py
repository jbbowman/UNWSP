'''
Developer: Jack Bowman
Program: 3-13 Shipping Charges
Date: 01/24/2022
'''

try:
    packageWeight = float(input('Enter the weight of the package in lbs: '))
    # gets package weight from user

    if packageWeight <= 2:
        print(f'Your package will cost ${1.5 * packageWeight:,.2f} to ship')
    elif packageWeight <= 6:
        print(f'Your package will cost ${3 * packageWeight:,.2f} to ship')
    elif packageWeight <= 10:
        print(f'Your package will cost ${4 * packageWeight:,.2f} to ship')
    else:
        print(f'Your package will cost ${4.75 * packageWeight:,.2f} to ship')
    # calculates and displays cost of shipping based on package weight

except Exception:

