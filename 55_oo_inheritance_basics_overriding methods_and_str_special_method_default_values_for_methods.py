# 55 56 57 OO Inheritance Basics, Overriding Methods, Overriding __str__ special_method_default_values_for_methods

# Python conventions:
# 2. Class names should use CapWords convention.
# 3. Variables should use thisStyle convention.
# 4. Always use self for the first argument to instance methods.
# 5. When writing method prototypes, use the pass keyword as placeholder
# 6. Multiline comments should use the # symbol for each line. Don't use docstring.


class Automobile:
    ''' -> Automobile base / parent class'''
    model_year = "2010"

    def start(self):
        print("Automobile is starting.....skrrt skrrt skrrt")

    def turn_off(self):
        '''-> Shut off Automobile...'''
        print("Click, sput, sput.......Vehicle is now off.")


class Truck(Automobile):
    '''-> Truck is a type of automobile. Inherits from Automobile and has all methods'''

    def __init__(self, year=None):
        if year is None:
            self.year = 2019
        else:
            self.year = year

    def __str__(self, year=None):
        return "2019 Truck sold by StudioWeb."

    def dumpLoad(self, load=None):
        if load is None:
            print("Truck has nothing to dump!!!!")
        else:
            print("Truck is dumping " + str(load) + " plumbusses!!!")
            print("Yeah straight dumpin dem loads!!!")

    def start(self):  # overriding method
        print("Truck is starting.......puta puta puta boom!!!!!")

    def turn_off(self):  # overriding method
        print("......Truck cut off without any noise!")

    def truckYear(self):
        print("This truck was built in " + str(self.year))


myTruck = Truck("2022")
myTruck.truckYear()

myTruck.start()
myTruck.turn_off()
print(myTruck)  # normally prints location in RAM but with __str__ it returns something instead

anotherTruck = Truck()
anotherTruck.truckYear()

emptyDumpTruck = Truck()
emptyDumpTruck.dumpLoad()

fullDumpTruck = Truck()
fullDumpTruck.dumpLoad(15000)

print(type(anotherTruck))
