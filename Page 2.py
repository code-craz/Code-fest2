from tkinter import *
import tkinter as ttk
import pyttsx3

#Initialize tkinter
root=Tk()
root.title("Code fest health bot")

#Create function for emergency 

def emergency():
    new_win= Toplevel(root)
    new_win.title("Health bot emergency stage")

    var=StringVar
    Label(new_win, text="Is your emergency any of the folowing?").pack()
    Checkbutton(new_win, text="Option 1", variable=var, command=lambda:print("do...")).pack()
    Checkbutton(new_win, text="Option 2", variable=var, command=lambda:print("do...")).pack()

#Create chronic function
def chronic():
    #Create a new window
    new_win=Toplevel(root)
    new_win.title("Health bot chronic stage")
    #Ask for issue
    Label(new_win, text="Is your issue any of the folowing?").pack()
    var=StringVar
    Checkbutton(new_win, text="Option 1", variable=var, command=lambda:print("Sup")).pack()
    Checkbutton(new_win, text="Option 2", variable=var, command=lambda:print("Bro")).pack()

#Check if user is in an emergency. (Using buttons for check)
emcheck= Label(root, text= "Are you in an emergency?")
y= Button(root, text="Yes", command=emergency)
space= Label(root, text="      ")
n= Button(root, text="No", command=chronic)
#Place the checks and buttons
emcheck.grid(row=1, column=2)
y.grid(row=2, column=1)
space.grid(row=3, column=1)
n.grid(row=4, column= 1)

root.mainloop()