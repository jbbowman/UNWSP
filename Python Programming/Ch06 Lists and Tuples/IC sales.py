# Developer: Jack Bowman
# Program: sales
# Date: 02/18/2022

def main():
    # creates list of 4 weeks of sales
    dailySales4wks = [[110, 230, 430, 540, 120],
                      [760, 340, 540, 230, 450],
                      [560, 650, 430, 440, 220],
                      [220, 320, 120, 320, 430]]

    # finds the sum of each row/week
    loop = 0
    for row in dailySales4wks:
        loop += 1
        weeklySum = sum(row)
        print(f'The sum of week {loop}s sales is {weeklySum}')

if __name__ == '__main__':
    main()