'''
Developer: Jack Bowman
Program: 3-16 February Days
Date: 01/24/2022
'''

try:
    gender = input('Are you a (m)ale or (f)emale? ').lower()
    age = float(input('What is your age? '))
    # collects gender and age from gender
    HIGH = 1.5
    MEDIUM = 1.25
    LOW = 1.0

    if (gender == 'm' and age > 25) or (gender == 'f' and age < 25):
        print(f'Your car insurance factor is {MEDIUM}')
        # males over 25 and females under 25 have 1.25 factor
    elif gender == 'm' and age < 25:
        print(f'Your car insurance factor is {HIGH}')
        # males under 25 have 1.5 factor
    elif gender == 'f' and age > 25:
        print(f'Your car insurance factor is {LOW}')
        # females over 25 have 1.0 rate
    else:
        print('If you are 25, you do not have an insurance factor.')
        # people age 25 are not factored in

except Exception:
    print('Something went wrong!')
# captures unrecognized inputs
