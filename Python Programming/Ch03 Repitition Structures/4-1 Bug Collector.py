'''
Developer: Jack Bowman
Program: 4-1 Bug Collector
Date: 01/23/2022
'''

day = 0  # number of days bugs have been logged
totalBugs = 0  # total number of bugs

while True:  # establishes loop so multiple items can be entered
    bugs = input(f'Enter the number of bugs on day {day + 1:,}, or type "done" to end the program: ').lower()
    # collects number of bugs for the day
    try:
        totalBugs += int(bugs)  # adds bugs to totalBugs
        day += 1  # adds 1 day to day variable
        print(f'After {day:,} day(s), your running count is {totalBugs:,} bug(s).')
        # if the user enters an integer, the number will be added to the totalBugs
    except Exception:
        if bugs == 'done':
            print(f'You have exited the program. After {day:,} day(s), your total number of bugs is: {totalBugs:,}')
            break
        # if the user enters "done," the total number of bugs will be displayed and the loop will break
        else:
            print('Not a recognized input. Please try again.')
        # if the user's entry is not recognized, the message above will be displayed
