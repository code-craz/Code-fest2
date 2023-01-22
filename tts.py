from tkinter import *

root = Tk()

options = {'Bleeding' : ['cover the wound with a sterle clean or gauze cloth' , 'once covered tightly wrap a bandage to slow down blood flow' ,] , 'option 2' : ['list item w' , 'list item x' , 'list item y' , 'list item z']}
options = {'Severe pain ' : ['' , 'list item 2' , 'list item 3' , 'list item 4'] , 'option 2' : ['list item w' , 'list item x' , 'list item y' , 'list item z']}

options = sorted(options)

var = StringVar(root)
var.set('Choose an option')

option = OptionMenu(root, var, *options)
option.pack()

selection = StringVar()

def changeOption(*args):
    newSelection = options[var.get()]
    selection.set(newSelection)

var.trace('w', changeOption)

variable1 = # if option 1 was selected from the menu then this variable would contain list item 1
variable2 = # if option 1 was selected from the menu then this variable would contain list item 2
variable3 = # if option 1 was selected from the menu then this variable would contain list item 3
variable4 = # if option 1 was selected from the menu then this variable would contain list item 4

root.mainloop()