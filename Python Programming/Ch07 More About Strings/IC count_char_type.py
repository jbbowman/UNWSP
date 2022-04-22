# Developer: Jack Bowman
# Program: count_char_type
# Date: 02/23/2022

def main():
    file = open(input('Please enter a file name within the project that you would like to open: '), 'r')
    fileContents = file.read()

    # recorded variables in file
    upper = 0
    lower = 0
    digits = 0
    whitespace = 0

    # identifies various characters in file and counts upper, lower, digits, and spaces
    for character in fileContents:
        if character.isupper():
            upper += 1
        elif character.islower():
            lower += 1
        elif character.isdigit():
            digits += 1
        elif character.isspace():
            whitespace += 1

    file.close()

    print(f'''Totals:
    {upper} uppercase letters
    {lower} lowercase letters
    {digits} digits
    {whitespace} spaces''')

if __name__ == '__main__':
    try:
        main()
    except Exception as exception:
        print(f'The following error occurred: {exception}')