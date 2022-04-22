# Developer: Jack Bowman
# Program: 6-4 Item Counter
# Date: 02/10/2022

def main():
    fileName = 'numbers.txt'  # name of the file to be opened
    file = open(fileName)  # opens file
    average = avgFileLines(file)  # calls the avgFileLines function
    print(f'The average of the numbers in the file is {average:,}')  # prints the results

def avgFileLines(file):  # calculates average of the numbers on each line in the file
    count = 0  # number of times the loop ran or number of lines in the file
    sum = 0  # sum of the numbers in each line of the file
    for line in file:  # adds 1 to the count variable and the number in the line to the sum variable for every loop
        count += 1
        sum += float(line)
    average = sum / count  # divides sum by count
    return average  # returns the final average

if __name__ == '__main__':
    try:
        main()
    except IOError:  # catches IOErrors
        print('File not found')
    except Exception as exception:  # catches all other errors
        print(f'The following error occurred: "{exception}"')