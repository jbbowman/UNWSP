# Developer: Jack Bowman
# Program: courses
# Date: 02/16/2022

def main():
    # creates courses list
    courses = ['COS101', 'COS102', 'COS103', 'COS104', 'COS105', 'COS106', 'COS107', 'COS108', 'COS109', 'COS1010']
    userInput = input('Please enter a course ID: ').upper()
    # checks if user's input is in courses list
    if userInput in courses:
        print('The course is in the list!')
    else:
        print('That course is not on the list!')

if __name__ == '__main__':
    try:
        main()
    except Exception as exception:
        print(f'The following error occurred: {exception}')
