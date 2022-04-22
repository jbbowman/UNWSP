# Developer: Jack Bowman
# Program: Ex. 9-1 Course Information
# Date: 03/15/2022

def main():
    # creates courses dictionary with relevant info
    courses = {
        'CS101': [3004, 'Haynes', '8:00 a.m.'],
        'CS102': [4501, 'Alvarado', '9:00 a.m.'],
        'CS103': [6755, 'Rich', '10:00 a.m.'],
        'NT110': [1244, 'Burke', '11:00 a.m.'],
        'CM241': [1411, 'Lee', '1:00 p.m.'],
    }

    # asks user for course
    key = input('Please enter a course number or type "all" to see all courses: ').upper()

    # if the course is in the courses dictionary, it will display its relevant info
    if key in courses:
        print(
            f'Course: {key}'
            f'\n\tRoom Number: {courses[key][0]}'
            f'\n\tInstructor: {courses[key][1]}'
            f'\n\tMeeting Time: {courses[key][2]}'
        )

    # if the user types "all", all of the courses will be displayed
    elif key == 'ALL':
        for key, value in courses.items():
            print(
                f'Course: {key}'
                f'\n\tRoom Number: {value[0]}'
                f'\n\tInstructor: {value[1]}'
                f'\n\tMeeting Time: {value[2]}'
            )

    # if the input is not recognized, an error statement will be shown to the user
    else:
        print('That is not a valid input')


if __name__ == '__main__':
    try:
        main()
    except Exception as exception:
        print(f'The following error occurred: {exception}')
