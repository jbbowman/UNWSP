# Developer: Jack Bowman
# Program: friend_book
# Date: 03/14/2022

def main():
    # creates dictionary friend_book
    friend_book = {
        'John': 'St. Paul',
        'Bob': 'Minneapolis',
        'Robert': 'Bloomington',
        'Phil': 'Isanti',
        'Adam': 'Cedar'
    }

    print(friend_book)

    # adds two names to friend_book
    friend_book['Ron'] = 'Grasston'
    friend_book['Bill'] = 'Hampton'

    print(friend_book)

    # deletes two names to friend_book
    deletekey(friend_book, 'Ron')
    deletekey(friend_book, 'Bill')

    print(friend_book)

def deletekey(dictionary, key):  # deletes a key from a dictionary
    if key in dictionary:
        del dictionary[key]

if __name__ == '__main__':
    main()