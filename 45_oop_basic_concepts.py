# 45 object oriented python

# THIS IS THE CLASS


class Car():
    ''' A simple class that describes a car '''

    def __init__(self, model, cost):  # special reserve function for ALL PYTHON CLASSES
        ''' Initialize the object '''
        self.model = model
        self.cost = cost

    def start(self):
        ''' Start the car'''
        print(self.model.title() + " is now starting.")  # title() capitalizes first letter


# class vs object
# THIS IS THE OBJECT
myCar = Car("audi", "$98k")  # object instantiation - object is created from class
myCar.start()

print("\nCreating new car... \n")

mySecondCar = Car("ford", "$25k")  # object instantiation - object is created from class
mySecondCar.start()
