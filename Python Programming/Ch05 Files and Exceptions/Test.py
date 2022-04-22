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
    tries = 0
    while not is_integer(line) and tries < 3:
        print("Not an integer; please try again")
        tries += 1
        line = input(prompt)
    if tries == 3:
        quit()

    return int(line)

# prompts for a user's age and prints out
# the number of years until the user can retire
def main():
    age = get_int("How old are you? ")
    retire = 65 - age
    print("Retire in", retire, "years.")


main()