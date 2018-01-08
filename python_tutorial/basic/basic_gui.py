# -*- coding:utf-8 -*- 
# @date: 2018-01-09
# @author: rocky

from tkinter import *

import tkinter.simpledialog as dl
import tkinter.messagebox as mb

root = Tk()
w = Label(root,text = "Label Title")
w.pack()

mb.showinfo("Welcome","Welcome Message")
guess = dl.askinteger("Number","Enter a number")

output = "This is output message"
mb.showinfo("output: ",output)