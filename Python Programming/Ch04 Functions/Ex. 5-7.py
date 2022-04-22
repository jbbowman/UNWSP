# Developer: Jack Bowman
# Program: Ex. 5-7
# Date: 02/05/2022

# seat cost variables
costA = 20
costB = 15
costC = 10

def main():
    try:
        # gets class a, b, and c seats sold
        seatsA = int(input('Enter the number of Class A seats sold: '))
        seatsB = int(input('Enter the number of Class B seats sold: '))
        seatsC = int(input('Enter the number of Class C seats sold: '))

        # prints revenue results
        print(f'''Results...
        Class A Revenue: ${calcrev(A=seatsA):,.2f}
        Class B Revenue: ${calcrev(B=seatsB):,.2f}
        Class C Revenue: ${calcrev(C=seatsC):,.2f}
        Total Revenue: ${calcrev(seatsA, seatsB, seatsC):,.2f}''')

    except:
        print('The values entered were note recognized')

def calcrev(A=0, B=0, C=0):  # calculates revenues of seats sold in class a, b, and/or c
    A *= costA
    B *= costB
    C *= costC
    return A + B + C

if __name__ == '__main__':
    main()