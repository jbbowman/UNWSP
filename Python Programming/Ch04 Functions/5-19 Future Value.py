# Developer: Jack Bowman
# Program: Ex. 5-19 Future Value
# Date: 02/08/2022

def main():
    presentValue = float(input('What is the present value of the account $'))
    interestRate = (float(input('What is the monthly interest rate of the account? %'))) / 100
    time = int(input('How many months will the account accrue interest? '))
    # gets variables from user to calculate future value of an account earning compound interest

    futureValue = calcint(presentValue, interestRate, time)  # sends values to calint function

    print(f'The future value of the account is ${futureValue:,.2f}')  # displays future value of the account

def calcint(p, i, t):  # calculates future value of an account earning monthly compound interest
    futureValue = p * (1 + i) ** t  # utilizes compound interest formula
    return futureValue

if __name__ == '__main__':
    main()
