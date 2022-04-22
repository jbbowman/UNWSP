# Developer: Jack Bowman
# Program: phone_nbr
# Date: 02/23/2022

def main():
    # gets a phone number from user and creates a new variable for the converted phone number
    phoneNumber = input('Please enter a phone number with alpha characters to return numeric phone number: ').lower()
    newPhoneNumber = ''

    # establishes which letters are associated with each number
    two = ['a', 'b', 'c']
    three = ['d', 'e', 'f']
    four = ['g', 'h', 'i']
    five = ['j', 'k', 'l']
    six = ['m', 'n', 'o']
    seven = ['p', 'q', 'r', 's']
    eight = ['t', 'u', 'v']
    nine = ['w', 'x', 'y', 'z']

    # returns new value to newPhoneNumber based on original value
    for digit in phoneNumber:
        if digit.isalpha():
            if digit in two:
                newPhoneNumber += '2'
            elif digit in three:
                newPhoneNumber += '3'
            elif digit in four:
                newPhoneNumber += '4'
            elif digit in five:
                newPhoneNumber += '5'
            elif digit in six:
                newPhoneNumber += '6'
            elif digit in seven:
                newPhoneNumber += '7'
            elif digit in eight:
                newPhoneNumber += '8'
            elif digit in nine:
                newPhoneNumber += '9'
        else:
            newPhoneNumber += digit

    # prints outcome
    print(newPhoneNumber)

if __name__ == '__main__':
    try:
        main()
    except Exception as exception:
        print(f'The following error occurred: {exception}')