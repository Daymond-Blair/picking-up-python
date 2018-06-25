# 37 multi parameters, flow control, elif using functions in functions and data type conversion

# write the code as going along

# len() str()


def multiParameter(name, last):
    print("Your first name is " + name + " and your last name is " + last)
    if name == "Jojo":
        print("I think I got this!!")
    elif last == "Blair":
        print("test")
# type error name should be string!!! use nested function str() and len()
        print("OSU!!!! That first name has  " + str(len(name)) + " letters g!")
    else:
        print("You aint no gangsta!")


multiParameter("Joe", "Blair")
