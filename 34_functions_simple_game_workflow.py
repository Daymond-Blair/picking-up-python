# 34 functions, simple game and flow controls
import time
# define functions:


def displayLesson():
    time.sleep(1)
    print('''This is a multiline
    text string...
    Its pretty much the /*  */ of python!!! ''')


def useTime():
    print("Shut down requested. ")
    time.sleep(1)
    print("3 seconds to shutdown ...")
    time.sleep(2)
    print("Going offline ...")


def flowControl():
    answer = input("Do you want to learn about multiline string? (Yes or No)")

# if answer == "yes" or "y":

    if answer == ("yes" or "y"):
        displayLesson()
    else:
        useTime()
        print("End program")


# execute program
flowControl()
