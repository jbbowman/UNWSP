class Schedule:
    def __init__(self, ID):
        self.ID = ID
        self.driver = []

    def __str__(self):
        return f'{self.ID} {self.driver}'

    def AddDriver(self, driver):
        self.driver = driver

class Driver:
    def __init__(self, name, licenses):
        self.name = name
        self.licenses = licenses

    def __str__(self):
        return f'{self.name} {self.licenses}'

    def AddLicense(self, license):
        self.licenses.append(license)

class Vehicle:
    def __init__(self, plate, name):
        self.plate = plate
        self.name = name

    def __str__(self):
        return f'{self.plate} {self.name}'

    def __repr__(self):
        return f'{self.plate} {self.name}'

# Schedules
Schedule1 = Schedule(1)
Schedule2 = Schedule(2)

# Drivers
JohnAppleseed = Driver('John Appleseed', [1, 2, 3, 4])
BobVance = Driver('Bob Vance', [1, 2])

# Vehicles
Vehicle1 = Vehicle(1232423, 'Truck')

# Add drivers to schedules
Schedule1.AddDriver([JohnAppleseed.name, BobVance.name])



print(Schedule1.driver)
print(Vehicle1)
