'''
Developer: Jack Bowman
Program: 4-5 Average Rainfall
Date: 01/28/2022
'''

while True:  # establishes loop in case there is an unrecognized input in total years variable
    try:
        totalYears = int(input('Enter the number of years that rainfall is collected: '))
        # asks user how long the program should run
        year = 0  # counts number of times outer loop has run
        totalRain = 0  # collects each entry of rainfall

        while year < totalYears:
            year += 1  # adds 1 to the year counter
            month = 0  # count of how many times inner loop has run
            yearRain = 0  # collects rainfall entry; resets every inner loop

            while month < 12:  # 12 months in a year
                try:
                    rain = float(input(f'Enter the total rainfall in inches for year {year}, month {month + 1}: '))
                    # gets total rain by month
                    month += 1  # adds 1 to the month counter
                    totalRain += rain  # adds users total rain by month to total for all years
                    yearRain += rain  # adds users total rain by month to total for single year
                except Exception:
                    print('Unrecognized input. Please try again...')

            print('')
            print(f'The total rainfall for year {year} over 12 months was {yearRain:,.2f} inches')
            print(f'The average monthly rainfall for year {year} was {yearRain / 12:,.2f} inches')
            print('')
            # prints total and average rainfall for the relevant year

        if year > 1:
            averageRain = totalRain / (year * 12)  # calculates average rain for all years entered
            print('')
            print(f'The total rainfall after the {year} years ({year * 12} months) recorded was {totalRain:,.2f} '
                  f'inches')
            print(f'The average monthly rainfall over those same {year} years was {averageRain:,.2f} inches')
            print('')
            # prints average monthly rainfall for all years entered
            break
        else:
            break

    except Exception:
        print('Unrecognized input. Please try again...')
