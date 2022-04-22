# Developer: Jack Bowman
# Program: 02/11/2022
# Date: 02/11/2022

def main():
    while True:
        try:
            age = int(input('Please enter your age: '))
            print(f'Congrats! You are {age} years old.')
            break
        except ValueError:
            print('You did not print a valid integer.')
            userInput = input('Press enter to try again or type "exit" ').lower()
            if userInput == 'exit':
                quit()

if __name__ == '__main__':
    try:
        main()
    except Exception as exception:
        print(f'The following error occurred: "{exception}"')