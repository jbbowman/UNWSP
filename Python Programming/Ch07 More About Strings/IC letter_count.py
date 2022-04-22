# Developer: Jack Bowman
# Program: letter_count
# Date: 02/21/2022

def main():
    name = input('Please enter your name: ').lower()  # User enters their name
    occurrences = 0  # counts occurrences of a letter
    for character in name:  # loops through each character of a string
        if character == 'a':  # checks for the letter "a"
            occurrences += 1
    print(f'The letter "a" occurs {occurrences} time(s) in your name.')

if __name__ == '__main__':
    try:
        main()
    except Exception as exception:
        print(f'The following error occurred: {exception}')