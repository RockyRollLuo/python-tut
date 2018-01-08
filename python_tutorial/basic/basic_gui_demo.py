# -*- coding:utf-8 -*- 
# @date: 2018-01-09
# @author: rocky

from tkinter import *

import tkinter.simpledialog as dl
import tkinter.messagebox as mb

root = Tk()
w = Label(root,text = "Guess Number")
w.pack()

mb.showinfo("Welcome","Welcome To Guess Number Game")

number = 60

while True:
    guess = dl.askinteger("Number","What's your guess?")

    if guess == number:
        output = "Bingo! you are right"
        mb.showinfo("Hint",output)
        break
    elif guess<number:
        output = "the number is higher than the guess"
        mb.showinfo("Hint",output)
#         break
    else:
        output = "the number is less than the guess"
        mb.showinfo("Hint",output)
#         break
print("Done")