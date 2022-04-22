'''
Developer: Jack Bowman
Program: clock
Date: 02/04/2022
'''


def main():  # defines main function
    name = input('Enter your name: ')
    print(f'Your name is {name}.')
    address()  # calls address function
    print('Farewell.')


def address():  # defines address function
    address = input('Enter your complete address: ')
    print(f'Your address is {address}.')
    # gets address and prints address


main()  # calls main function
