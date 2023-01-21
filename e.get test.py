#Import the required libraries
from tkinter import *
from tkinter import ttk

#Create an instance of Tkinter Frame
root = Tk()

#Set the geometry
root.geometry("700x250")

# Define a function to return the Input data
def get_data():
   label.config(text= entry.get())

#Create an Entry Widget
entry = Entry(root, width= 42)
entry.place(relx= .5, rely= .5, anchor= CENTER)

#Inititalize a Label widget
label= Label(root, text="")
label.pack()

#Create a Button to get the input data
ttk.Button(root, text= "Click to Show", command= get_data).place(relx= .7, rely= .5, anchor= CENTER)

root.mainloop()