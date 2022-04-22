'''
Developer: Jack Bowman
Program: nested
Date: 01/28/2022
'''

for length in range(1, 11):  # the range of lengths is 1 through 10
    for width in range(1, 6):  # the range of widths is 1 through 5
        volume = length * width * 0.25  # length x width x height = volume
        print(f'If the dimensions are {length}, {width}, 0.25, the volume is {volume}')
        