# Developer: Jack Bowman
# Program: cities
# Date: 02/18/2022

def main():
    # creates a list and collects a place the user does not want to go
    cities = ['Minneapolis', 'St. Paul', 'Bloomington', 'Anoka', 'New Brighton']
    oldCity = input('Where would you not like to go? ')

    try:
        index = cities.index(oldCity)  # finds index of unwanted city
        newCity = input('Where would you like to go? ')
        cities[index] = newCity  # replaces unwanted city

        print(cities)
    except ValueError:
        print('The item is not in the list!')
if __name__ == '__main__':
    try:
        main()
    except Exception as exception:
        print(f'The following error occurred: {exception}')