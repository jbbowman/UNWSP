# Developer: Jack Bowman
# Program: cities
# Date: 03/16/2022

def main():
    # list of cities and their latitude
    cities = {
        'Nairobi': 1,
        'Johannesburg': 26,
        'Cairo': 30,
        'Abidjan': 5,
        'Khartoum': 15,
        'Zanzibar': 6
    }

    # creates new dictionary with cities in tropic of Cancer/Capricorn
    citiesTOC = {k:v for k,v in cities.items() if v < 23}

    print(citiesTOC)

if __name__ == '__main__':
    try:
        main()
    except Exception as exception:
        print(exception)
