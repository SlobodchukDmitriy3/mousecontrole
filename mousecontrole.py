from tkinter import *


def b1(event):
    print("Pushed right button of the mouse")


def b3(event):
    print("Pushed left button of the mouse")


def move(event):
    x = event.x
    y = event.y
    s = "Move the mouse {}x{}".format(x, y)
    root.title(s)
    root = Tk()
    root.minsize(width=400, height=300)
    root.bind('<Button-3>', b1)
    root.bind('<Button-1>', b3)
    root.bind('<Motion>', move)
    root.mainloop()
