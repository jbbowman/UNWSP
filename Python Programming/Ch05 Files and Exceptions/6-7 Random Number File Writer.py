# Developer: Jack Bowman
# Program: 6-7 Random Number File Writer
# Date: 02/11/2022

import random  # program utilizes randint function

def main():
    numbers = int(input('How many random numbers would you like written in the file? '))
    randList(numbers)  # calls randList function and sends users argument above

def randList(loopcap):  # writes a random list of numbers onto a file named "numbers.txt"; user determines length
    fileName = open('numbers.txt', 'w')
    numRange = 500  # random numbers are between 1 and numRange variable
    loops = 0
    while loops < loopcap:
        fileName.write(str(random.randint(1, numRange)) + '\n')
        loops += 1

if __name__ == '__main__':
    try:
        main()
        print('The program ran successfully. '
              'A file named "numbers.txt" has been created with a list of random numbers')
    except ValueError:
        print('An invalid integer was entered.')
    except Exception as exception:
        print(f'''The following error occurred while running the program: 
    {exception}''')
