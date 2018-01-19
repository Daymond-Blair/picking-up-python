#37, 38, 39 multiple parameters in functions
#more flow control with elif, using functions in functions
#and (data)type conversion.

def multipleParameter(firstName, lastName):
    print("Your first name is " + firstName + " and your last name is " + lastName)
    if firstName == "Daymond":
        print("Looks like an if statement to me!\n")
    elif firstName == "Jimi":
        print("Wah waaaah waaaaaaaaaah\n")
    elif (firstName == "Calvin" or lastName == "Hicks"):
        print("The darker the night, the brighter the stars!!!\n")
    elif firstName == "Elizabeth" or lastName == "Smith":
        print("Imma Lizzard Wizzard!!!!\n")
    else:
        print("Looks like an else statement to me!\n")


#run program

multipleParameter("Daymond", "Blair")

multipleParameter("Jack", "Brisco")

multipleParameter("Elizabeth", "Smith")

multipleParameter("Calvin", "Jackson")

multipleParameter("James", "Hicks")
