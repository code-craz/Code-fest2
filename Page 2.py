from tkinter import *
import tkinter as ttk
import pyttsx3

root=Tk()
root.title("Code fest health bot")



def emergency():
    new_win= Toplevel(root)
    new_win.title("Health bot emergenc stage")

    var=StringVar
    Label(new_win, text="Is your emergency any of the folowing?").pack()
    Checkbutton(new_win, text="Option 1", variable=var, command=lambda:print("Sup")).pack()
    Checkbutton(new_win, text="Option 2", variable=var, command=lambda:print("Bro")).pack()

emcheck= Label(root, text= "Are you in an emergency?")
y= Button(root, text="Yes", command=emergency)
space= Label(root, text="      ")
n= Button(root, text="No")

emcheck.grid(row=1, column=2)
y.grid(row=2, column=1)
space.grid(row=3, column=1)
n.grid(row=4, column= 1)

root.mainloop()