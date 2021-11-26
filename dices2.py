from tkinter import *
import random as randint

win = Tk()
win.title("Dices")
o = [PhotoImage(file="./pic/one.png"), PhotoImage(file="./pic/two.png"), PhotoImage(file="./pic/three.png"),
     PhotoImage(file="./pic/four.png"), PhotoImage(file="./pic/five.png"), PhotoImage(file="./pic/six.png")]


def start():
    global la
    la.config(image=o[randint(0, 5)])


la = Button(win, image=PhotoImage(file="./pic/START.png"), command=start)
la.pack()

win.mainloop()
