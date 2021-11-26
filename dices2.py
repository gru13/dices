from tkinter import *
import random as randint

win = Tk()
win.title("Dices")
o = [PhotoImage(file="./pic/one.png"), PhotoImage(file="./pic/two.png"), PhotoImage(file="./pic/three.png"),
     PhotoImage(file="./pic/four.png"), PhotoImage(file="./pic/five.png"), PhotoImage(file="./pic/six.png")]


def start():
    global la
    y = randint(0, 5)
    la.config(image=o[y])


la = Button(win, image=PhotoImage(file="./pic/START.png"), command=start)
la.pack()

win.mainloop()
