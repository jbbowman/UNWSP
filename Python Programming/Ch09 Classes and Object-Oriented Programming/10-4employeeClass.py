# Developer: Jack Bowman
# Program: Ex. 10-4 Employee Class
# Date: 03/16/2022

class Department:
    # creates attributes of departments
    def __init__(self, name):
        self.name = name

    # represent department objects as strings
    def __str__(self):
        return self.name

class Title:
    # creates attributes of titles
    def __init__(self, name):
        self.name = name

    # represent title objects as strings
    def __str__(self):
        return self.name

class Employee:
    # creates attributes of employees
    def __init__(self, id, firstName, lastName, department, title):
        # establishes referential integrity
        if not isinstance(department, Department):
            raise TypeError('Department does not exist')
        if not isinstance(title, Title):
            raise TypeError('Title does not exist')

        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.department = department
        self.title = title

    # represent employee objects as strings
    def __str__(self):
        return f'ID = {self.id}\n' \
               f'Name = {self.firstName} {self.lastName}\n' \
               f'Department = {self.department}\n' \
               f'Job Title = {self.title}\n'

# creates instances of departments
department = {
    'Accounting': Department('Accounting'),
    'IT': Department('IT'),
    'Manufacturing': Department('Manufacturing')}

# creates instances of titles
title = {
    'Vice President': Title('Vice President'),
    'Programmer': Title('Programmer'),
    'Engineer': Title('Engineer')}

# creates instances of employees
employee = {
    47899: Employee(47899, 'Susan', 'Meyers', department['Accounting'], title['Vice President']),
    39119: Employee(39119, 'Mark', 'Jones', department['IT'], title['Programmer']),
    81774: Employee(81774, 'Joy', 'Roger', department['Manufacturing'], title['Engineer'])}

for key, value in employee.items():
    print(value)

