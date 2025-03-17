
# Importing dependencies
import tkinter as tk
from tkinter import *
import random


# Creating a GUI Window
window = Tk()
window.title("Dice Roller")

e = Entry(window, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    e.delete(0, END)
    global n
    n = number
    dice = random.randint(1, n)
    e.insert(0, dice)


def button_click_clear():
    e.delete(0, END)


# Define Buttons
button_1 = Button(window, text="d_2", padx=35, pady=20, command=lambda: button_click(2))
button_2 = Button(window, text="d_4", padx=35, pady=20, command=lambda: button_click(4))
button_3 = Button(window, text="d_6", padx=33, pady=20, command=lambda: button_click(6))
button_4 = Button(window, text="d_8", padx=35, pady=20, command=lambda: button_click(8))
button_5 = Button(window, text="d_10", padx=32, pady=20, command=lambda: button_click(10))
button_6 = Button(window, text="d_12", padx=30, pady=20, command=lambda: button_click(12))
button_7 = Button(window, text="d_20", padx=32, pady=20, command=lambda: button_click(20))
button_8 = Button(window, text="d_100", padx=29, pady=20, command=lambda: button_click(100))
button_9 = Button(window, text="Clear", padx=29, pady=20, command=button_click_clear)

# Put Buttons on screen
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

# This tells Python to run the Tkinter event loop.
window.mainloop()
