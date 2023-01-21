from tkinter import *
import tkinter as ttk
import pyttsx3

#Initialize tkinter
root=Tk()
root.title("Code fest health bot")

#find the user's name
nametxt= Label(root, text="What is your name?")
name= Entry(root)
#find the user's doctor name
docnumb= Label(root, text= "What is your doctor's number?")
docn= Entry(root)
#Create function for opening page 2
def openpage2():
    open("Page 2.py")


#Open page 2
p2op= Button(root, text="Open next page", command=openpage2)
#Postition the questions 
nametxt.grid(row=1, column= 1)
name.grid(row=2, column=1)
docnumb.grid(row=3, column=1)
docn.grid(row=4, column=1)
#Position the button
p2op.grid(row=5, column=1)

root.mainloop()