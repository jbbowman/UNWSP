# Developer: Jack Bowman
# Program: Ex. 5-5
# Date: 02/05/2022

TAX = 0.0072  # tax constant


def main():
    landValue = float(input('Enter the value of your property: $'))
    # gets the lands actual value from user

    assessmentValue = assess(landValue)
    propertyTax = assessmentValue * TAX
    # calls assess function and calculates property tax

    print(f'The assessment value of your property is ${assessmentValue:,.2f}')
    print(f'Your property tax is ${propertyTax:,.2f}')
    # prints assessment value and total property tax


def assess(value):  # calculates and returns assessment value
    assessmentValue = value * 0.6
    return assessmentValue


if __name__ == '__main__':
    main()
