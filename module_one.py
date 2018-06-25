# module one

''' module 1 '''

import turtle
import tkinter


def a_function():
    print("A function has been fired!")


class Dog():

    def bark(self):
        print("The dog barks!\n")

    def dog_draw_square(self):
        t = turtle.Pen()
        for x in range(1, 5):
            t.forward(50)
            t.left(90)
            print("Dog has done its job drawing.")

    def dog_spawn_window(self):
        tk = tkinter.Tk()
        btn = tkinter.Button(tk, text="click to draw", command=self.dog_draw_square)
        btn.pack()
