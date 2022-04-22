'''
Developer: Jack Bowman
Program: product
Date: 02/04/2022
'''

def main():
    value1 = int(input('Please enter the first value you would like multiplied: '))
    value2 = int(input('Please enter the second value you would like multiplied: '))
    # Gets two values from user

    product = calc(value1, value2)
    # calls the calc function to multiply the two values together

    print(f'The product is {product}')
    # displays the final product

def calc(num1, num2):
    product = num1 * num2
    return product

# calc function multiplies two parameters and returns the product

main()
# calls main function
