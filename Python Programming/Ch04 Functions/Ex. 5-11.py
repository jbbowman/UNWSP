# Developer: Jack Bowman
# Program: Ex. 5-11
# Date: 02/05/2022

import random

def main():
    print('Welcome to the math problem generator.')
    print('Type quit at any time to stop the program.')
    input('Press enter to continue...')
    quiz()

def quiz():
    correct = attempts = 0
    # records correct and incorrect answers

    while True:
        num1 = random.randint(1, 1001)
        num2 = random.randint(1, 1001)
        answer = add(num1, num2)
        # creates two random integers and adds them together

        while True:
            guess = input(f'What is {num1} + {num2}? ').lower()
            # asks the user to input their guess for the addition problem

            if guess == str(answer):  # if the user is correct, they get a new problem
                print('That is correct!')
                attempts += 1
                correct += 1
                break
            elif guess == 'quit':  # if the user types "quit" the program stops
                print('Exiting the program...')
                print(f'You got {correct}/{attempts} correct.')
                quit()
            else:  # if the user enters anything else, it is considered incorrect
                print('That is incorrect! Please try again, or type quit to stop the program.')
                attempts += 1

def add(num1, num2):  # creates function that adds two numbers
    answer = num1 + num2
    return answer

if __name__ == '__main__':
    main()
