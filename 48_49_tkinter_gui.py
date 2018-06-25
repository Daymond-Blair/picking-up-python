# 48 49 tkinter gui

from tkinter import *  # MODULE/PACKAGE that contains many many classes - * means import ALL OF THESE CLASSES FOR USE

root = Tk()  # instance of Class Tk() from MODULE TKINTER aka OBJECT!!!
pythonCourseLogo = PhotoImage(file="giphy-downsized.gif")  # photo image function grabs image file

rightLabel = Label(root, image=pythonCourseLogo)
rightLabel.pack(side="right")

myText = ''' With tkinter, YOU CAN ONLY USE GIF IMAGES. There are other, more powerful Python packages that allow you to use other image types.'''

myOtherText = "LOOK AT DAT PUG!!!"
# call title method (from class Tk()) - title of python window at very top
root.title("Our amazing Python window!!")

leftLabel = Label(root, justify=RIGHT, padx=10, text=myOtherText).pack(side="left")

'''w = Label(root, text = "Hello Tkinter - one of Python's tools for creating GUIs!") # instance of Class Label() aka Label OBJECT!!!
w.pack() # call pack method (from class Label()) - packs label text into window'''

print("launching window ...")
root.mainloop()  # mainloop() keeps code running until window is closed
