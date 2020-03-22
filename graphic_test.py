#!/usr/bin/env python
# _*_ coding:utf-8 _*_

#This program is to test the graphic codes from the book <Python for Kids>.

from tkinter import *
import random

def hello():
    print("hello there")

def random_rectangle(width, height):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    canvas.create_rectangle(x1, y1, x2, y2)

#The tkinter main window to hold everything in tkinter.

tk = Tk()

#Define the widgets.
btn = Button(tk, text = 'Click me', command = hello)
#Add the widget to the main window.
btn.pack()

canvas = Canvas(tk, width = 500, height = 500)
canvas.pack()

for x in range(0, 10):
    random_rectangle(400, 400)

#The meesage loop
tk.mainloop()
