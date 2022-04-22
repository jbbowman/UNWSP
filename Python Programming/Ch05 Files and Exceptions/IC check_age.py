# Returns True if s can be converted to type int.

def is_integer(s):
    try:
        s = int(s)
        return True
    except ValueError:
        return False

# Repeatedly prompts for input until a numeric string is typed.
# Returns the int value that was typed by the user.
def get_int(prompt):
    line = input(prompt)
    while not is_integer(line):
        userInput = input("Not an integer; press enter to try again or type 'quit' to quit the program: ").lower()
        if userInput == 'quit':
            print('You have exited the program.')
            quit()
        line = input(prompt)

    return int(line)

# prompts for a user's age and prints out
# the number of years until the user can retire
def main():
    age = get_int("How old are you? ")
    retire = 65 - age
    print("Retire in", retire, "years.")


main()