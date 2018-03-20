# 35 function arguments, parameters, and return values


def nameFunction(name):
    print("Your name is: " + name)


def lastNameFunction(lastName):
    print("Oh....your last name is " + lastName)
    #print("So youre telling me your name is " + firstName + lastName)


def getName():
    name = input("What is your name: ")
    return name


def getLastName():
    lastName = input("Ok.....cool, but whats your last name: ")
    return lastName


def keepRunning():
    lastNameFunction(getLastName())


def runIt():
    print("Start the app ...")
    nameFunction(getName())


def finish():
    print(nameFunction(getName()))
    print(lastNameFunction(getLastName))


# run the program
runIt()
keepRunning()
#finish()

#name = "david"
# print(name)
