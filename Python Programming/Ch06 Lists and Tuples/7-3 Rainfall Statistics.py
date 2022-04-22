# Developer: Jack Bowman
# Program: 7-3 Rainfall Statistics
# Date: 02/19/2022

import statistics

def main():
    global month
    rainfall = []

    # collects rainfall data
    for month in range(12):
        monthlyRainfall = float(input(f'Please enter the amount of rainfall in inches for month {month + 1}: '))
        rainfall.append(monthlyRainfall)

    # finds sum and mean of rainfall
    totalRain = sum(rainfall)
    avgRain = statistics.mean(rainfall)

    # finds all months that have min/max rainfall
    lowRainMonth = search(rainfall, min(rainfall))
    highRainMonth = search(rainfall, max(rainfall))

    print(f'''
Total amount of rain over {month + 1} months = {totalRain:,.2f} inches
Average amount of rain over {month + 1} months = {avgRain:,.2f} inches
Month(s) with lowest amount of rain = Month {lowRainMonth}
Month(s) with highest amount of rain = Month {highRainMonth}''')

def search(list, query):  # finds instances of an item in a list and returns index/indices + 1
    results = []
    for index in range(len(list)):
        if list[index] == query:
            results.append(index + 1)
    return (str(results)).strip('[]')

if __name__ == '__main__':
    try:
        main()
    except ValueError:
        print('Invalid input; input must be numeric')
    except Exception as exception:
        print(f'The following error occurred: {exception}')