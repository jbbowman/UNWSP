# Developer: Jack Bowman
# Program: interstates
# Date: 03/16/2022

def main():
    routes = {
        'MN': 35,
        'SF': 80,
        'SE': 90,
        'WA': 94,
        'MI': 95,
        'TC': 494,
    }

    routesEW = {k:v for k,v in routes.items() if v % 2 == 0}
    importantRoutes = {k:v for k,v in routesEW.items() if v % 5 == 0}

    print(f'List of routes: {routes}')
    print(f'East/West routes: {routesEW}')
    print(f'Important routes: {importantRoutes}')

if __name__ == '__main__':
    try:
        main()
    except Exception as exception:
        print(exception)
