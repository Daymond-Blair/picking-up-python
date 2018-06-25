# 60 opening files with python

# 3 ways to structure code
# how to better handle errors with: exceptions
# file manipulation

# with open('system_config.txt') as file_object:  # open system_config and store it as a file object called contents
# contents = file_object.read()
# print(contents)

'''def openFile():  # open file function by hard-coding file name

    with open('system_config.txt') as file_object:
        contents = file_object.read()
        print(contents)


def openFile2(file):  # open file function by passing argument
    with open(file) as file_object:
        contents = file_object.read()
        print(contents)


openFile2('system_config.txt')'''

# C:\Users\D\Desktop\Python Master\Coursework


class Filer:

    def openFile(self):  # open file function by hard-coding file name
        # try:
        with open('system_config.txt') as file_object:
            contents = file_object.read()
            print(contents)
        # except

    def openFile2(self, file):  # open file function by passing argument
        with open(file) as file_object:
            contents = file_object.read()
            print(contents)


myFiler = Filer()

myFiler.openFile2('C:\\\Users\\\D\\\Desktop\\\Python Master\\\Coursework\\\people.txt')
