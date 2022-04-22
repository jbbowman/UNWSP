'''
Developer: Jack Bowman
Program: 3-3 Age Classifier
Date: 01/24/2022
'''

INFANT_UPPER_LIMIT = 1
CHILD_UPPER_LIMIT = 13
TEENAGER_UPPER_LIMIT = 20
# constants that identify age classifications

try:
    age = float(input('Enter a persons age: '))
    # gets user's age

    if age < INFANT_UPPER_LIMIT:
        print('This person is considered an infant')
    elif age < CHILD_UPPER_LIMIT:
        print('This person is considered child')
    elif age < TEENAGER_UPPER_LIMIT:
        print('This person is considered a teenager')
    elif age >= TEENAGER_UPPER_LIMIT:
        print ('This person is considered an adult')
    # classifies individual based on age that was entered

except Exception:
    print('Something went wrong!')
# try and except statement collects unrecognized inputs
