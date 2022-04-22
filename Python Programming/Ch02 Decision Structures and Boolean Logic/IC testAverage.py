'''
Developer: Jack Bowman
Program: testAverage2
Date: 01/19/2022
'''

A = 90
B = 80
C = 70
D = 60
# grade constants

try:
    score1 = int(input('Please enter the first test score: '))
    score2 = int(input('Please enter the second test score: '))
    score3 = int(input('Please enter the third test score: '))
    average = (score1 + score2 + score3)/3
    # collects scores and their average

    if average >= A:
        print('You got an A!')
    elif average >= B:
        print('You got a B')
    elif average >= C:
        print('You got a C')
    elif average >= D:
        print('You got a D')
    elif average < D:
        print('You got an F')
    # displays grade based on score

except Exception:
    print('Something went wrong!')
# try and except statement traps incorrect inputs
