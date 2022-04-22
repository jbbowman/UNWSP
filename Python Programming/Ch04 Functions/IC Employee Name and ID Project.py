# get employee name and assign an ID

count = 0


def main():
    first = input('Enter employee first name: ')
    last = input('Enter employee last name: ')
    # global count
    employee(first, last)


def employee(name1, name2):
    global count
    # count = count + 1
    count += 1

    print('Employee: ' + name1 + ' ' + name2)
    print('Employee ID: ' + str(count))


main()