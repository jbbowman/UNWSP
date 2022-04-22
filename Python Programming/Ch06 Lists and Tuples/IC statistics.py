# Developer: Jack Bowman
# Program: statistics
# Date: 02/18/2022

import statistics

def main():
    # creates a scores list with 10 values and gets the average, min., and max score
    scores = [100, 80, 90, 63, 75, 83, 71, 94, 99, 80]
    minScore = min(scores)
    maxScore = max(scores)
    avgScore = statistics.mean(scores)

    # prints results
    print(f'''
The minimum test score was {minScore}
The maximum test score was {maxScore}
The average test score was {avgScore}''')

if __name__ == '__main__':
    try:
        main()
    except Exception as exception:
        print(f'The following error occurred: {exception}')