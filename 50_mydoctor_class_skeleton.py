# 50 51 52 53 MyDoctor - class skeleton - instantiation - docstrings


class MyDoctor:
    ''' -> MyDoctor class docstring...... tell programmers about this class. Its pretty much a small explanation of what this class does'''

    def sayHi(self):
        print("Heya")

    def sayBye(self):
        print("Peace")

    def askDocQuestion(self):
        question = input("You look like you could use a health tip. Go for it? Y/N. ")
        if question == 'Y' or question == 'y':
            print("Oh okay then well great! Glad you said " + question + "; lets get started....\n")
        elif question == 'N' or question == 'n':
            print("Oh so you ain't really lookin for no wrestler.\n")
        else:
            print("Come again?\n")


print("Running!\n")

drCurry = MyDoctor()

x = ''

'''while x != 'Y' or x != 'y' or x != 'N' or x != 'n':
    drCurry.askDocQuestion()'''

drCurry.askDocQuestion()

drCurry.sayHi()

drCurry.sayBye()
