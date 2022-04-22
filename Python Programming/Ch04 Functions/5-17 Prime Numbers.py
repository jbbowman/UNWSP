# Developer: Jack Bowman
# Program: Ex. 5-17 Prime Numbers
# Date: 02/08/2022

def main():
    number = int(input('Enter a number to see if it is prime: '))  # gets number from user

    if is_prime(number):  # calls is_prime function to determine if the number above is prime
        print('The number is prime')
    else:
        print('The number is composite')

def is_prime(val):  # determines if a number is prime
    if val < 2:  # numbers less than two are not prime
        return False
    elif val == 2:  # 2 is prime
        return True
    else:
        for n in range(2, val):  # tests every other possibility between 2 and the value the user entered
            if val % n == 0:
                return False
    return True

if __name__ == '__main__':
    main()