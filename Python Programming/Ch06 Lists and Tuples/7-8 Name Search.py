# Developer: Jack Bowman
# Program: 7-8 Name Search
# Date: 02/19/2022

def main():
    # calls filelist function
    boyNames = filelist('BoyNames.txt')
    girlNames = filelist('GirlNames.txt')

    # gets the name to compare to the names lists
    userInput = input('Please enter a name to see if it is among the most 200 most popular names '
                      'between 2000 and 2009: ').lower()

    # checks whether the users inputted name is on either list
    if userInput in boyNames or userInput in girlNames:
        print('The name was among the most popular during this period.')
    else:
        print('The name was not among the most popular during this period.')

def filelist(file):  # appends file lines onto a list
    List = []
    file = open(file, 'r')
    for line in file:
        List.append((line.strip('\n')).lower())
    return List


if __name__ == '__main__':
    try:
        main()
    except ValueError:
        print('Invalid input; input must be numeric')
    except Exception as exception:
        print(f'The following error occurred: {exception}')
