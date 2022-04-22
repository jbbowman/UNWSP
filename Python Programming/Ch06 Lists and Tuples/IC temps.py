# Developer: Jack Bowman
# Program: temps
# Date: 02/16/2022

def main():
    temp = []  # instantiates a list
    for num in range(7):
        # appends additional number to list
        temp.append(float(input(f'Enter the low temperature for day {num + 1} of 7: ')))
    average = sum(temp) / 7  # gets average of the temp list
    print(f'The average low temperature is {average}')

if __name__ == '__main__':
    try:
        main()
    except Exception as exception:
        print(f'The following error occurred: {exception}')
