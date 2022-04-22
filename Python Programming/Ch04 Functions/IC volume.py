# Developer: Jack Bowman
# Program: volume in-class
# Date: 02/07/2022

def main():
    length = float(input('Enter the length of the object: '))
    width = float(input('Enter the width of the object: '))
    height = float(input('Enter the height of the object: '))
    # gets dimensions of an object from user

    print(f'The volume of the object is {calcvolume(length, width, height):,} units')
    # calls volume function and prints results

def calcvolume(l, w, h):  # calculates volume by multiplying the length, width and height
    volume = l * w * h
    return volume

if __name__ == '__main__':
    main()