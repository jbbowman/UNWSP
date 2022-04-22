# Developer: Jack Bowman
# Program: 6-2 File Head Display
# Date: 02/10/2022

def main():
    file = input('Please enter the name of the file you would like to read: ')  # gets file name from user
    openfile(file)  # calls openfile function

def openfile(name):  # opens and reads first five lines of a file
    file = open(name, 'r')  # opens file
    currentLine = 0  # count for current line number in the loop below
    for line in file:
        # prints all lines up to the fifth line or when a line is blank
        if currentLine < 5 and line != '':
            currentLine += 1
            print(line, end='')

if __name__ == '__main__':
    try:
        main()
    except IOError:  # catches IOErrors
        print('File not found')
    except Exception as exception:  # catches all other errors
        print(f'The following error occurred: {exception}')