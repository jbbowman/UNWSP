'''
Developer: Jack Bowman
Program: employee_count
Date: 02/04/2022
'''

count = 0

def main():
    fname = input('Please enter your first name: ')
    lname = input('Please enter your last name: ')
    # gets first and last name of the user

    employee(fname, lname)
    # calls employee function

def employee(first, last):
    print(f'Your name is {first} {last}')
    # concatenates first and last name of user

    global count
    count += 1
    # assigns an EmployeeID that is 1 greater than the previous users EmployeeID

    print(f'Your EmployeeID is {count}')
    # prints the users EmployeeID

if __name__ == '__main__':
    while True:
        main()
        userInput = input('Press enter to continue or type exit to exit... ')
        if userInput == 'exit':
            break
        else:
            main()
    # calls main function and allows user to enter multiple names
