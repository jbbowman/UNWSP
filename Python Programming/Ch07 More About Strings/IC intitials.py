# Developer: Jack Bowman
# Program: initials
# Date: 02/21/2022

def main():
    fullName = input('Please enter your full name: ')

    name = fullName.split(' ')  # splits full name into names separated by spaces

    # gets first letter of every name inputted, capitalizes it, and separates it with periods
    for character in name:
        print(character[0].upper(), sep='', end='')
        print('.', sep= '', end='')

if __name__ == '__main__':
    main()