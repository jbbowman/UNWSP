# Developer: Jack Bowman
# Program: friends
# Date: 02/16/2022

def main():
    friends = ['Jim', 'Bob', 'Bill', 'Rob', 'Tim']  # creates a list of 5 names
    index = 0
    while index < len(friends):  # prints all names in the friends list
        print(friends[index])
        index += 1
    print('--------')

    # changes first two names in the list
    friends[0] = 'Ron'
    friends[1] = 'Phil'
    index = 0
    while index < len(friends):  # prints list again
        print(friends[index])
        index += 1

if __name__ == '__main__':
    try:
        main()
    except Exception as exception:
        print(f'The following error occurred: {exception}')
