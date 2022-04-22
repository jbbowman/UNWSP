# Developer: Jack Bowman
# Program: 6-4 Item Counter
# Date: 02/10/2022

def main():
    fileName = 'names.txt'  # name of the file that will be examined for number of lines
    file = open(fileName, 'r')  # opens file above
    lines = countlines(file)  # calls the countlines function to get the number of lines in the file
    print(f'There are {lines} lines in this file')  # prints result


def countlines(file):  # counts lines in a file
    count = 0  # running count of lines in file
    for lines in file:
        count += 1
    return count

if __name__ == '__main__':
    try:
        main()
    except IOError:  # catches IOErrors
        print('File not found')
    except Exception as exception:  # catches all other errors
        print(f'The following error occurred: "{exception}"')
