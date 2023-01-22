from tkinter import *
import tkinter as ttk
import pyttsx3
import sys

def Page_2():
    p2= Toplevel(root)
    #Check if user is in an emergency. (Using buttons for check)
    emcheck= Label(p2, text= "Are you in an emergency?")
    y= Button(p2, text="Yes", command=emergency)
    space= Label(p2, text="      ")
    n= Button(p2, text="No", command=chronic)
    #Place the checks and buttons
    emcheck.grid(row=1, column=2)
    y.grid(row=2, column=1)
    space.grid(row=3, column=1)
    n.grid(row=4, column= 1)



root= Tk()
#find the user's name
nametxt= Label(root, text="What is your name?")
name= Entry(root)
#find the user's doctor name
docnumb= Label(root, text= "What is your doctor's number?")
docn= Entry(root)
p2op= Button(root, text= "Next", command=Page_2)
#Create function for opening page 2
 


#Open page 2

#Postition the questions 
nametxt.grid(row=1, column= 1)
name.grid(row=2, column=1)
docnumb.grid(row=3, column=1)
docn.grid(row=4, column=1)
#Position the button
p2op.grid(row= 5, column=2)
def get_dict():
    return {'bleeding': 'Cover the wound with sterile gauze or a clean cloth.', 
'breathing difficulties': 'Check the persons airway, breathing, and pulse and loosen any tight clothing.', 
'someone collapses': 'Loosen belts, collars or other constrictive clothing.', 
'fit or epißleptic seizure': 'Cushion their head if they\'re on the ground and loosen any tight clothing around their neck, such as a collar or tie, to aid breathing then turn them to thier side.', 
'severe pain': 'Get some gentle exercise or Breathe right to ease pain.', 
'heart attack': 'Chew and swallow an aspirin while waiting for emergency help or Begin CPR if the person is unconscious.', 
'a stroke': 'Call 911 and perform CPR.'}

#Initialize tkinter
root.title("Code fest health bot")

#Aarav place background pic


#Create function for emergency 

def emergency():
    call_win= Toplevel(root)
    call_win.title("Initialize call")

    Label(call_win, text= "Iitializing call, number"+ docn.get()).pack()
    #Create a new window
    new_win= Toplevel(root)
    new_win.title("Health bot emergency stage")

    #Create input field and match with dictionary 
    a_dict = {'bleeding': 'Cover the wound with sterile gauze or a clean cloth.', 
'breathing difficulties': 'Check the persons airway, breathing, and pulse and loosen any tight clothing.', 
'collpase': 'Loosen belts, collars or other constrictive clothing.', 
'fit' or 'epileptic seizure': 'Cushion their head if they\'re on the ground and loosen any tight clothing around their neck, such as a collar or tie, to aid breathing then turn them to thier side.', 
'severe pain': 'Get some gentle exercise or Breathe right to ease pain.', 
'heart attack': 'Chew and swallow an aspirin while waiting for emergency help or Begin CPR if the person is unconscious.', 
'stroke': 'Call 911 and perform CPR.'}



    # Define a function to return the Input data
    def get_data():
        
        #Check if key in dictioary and print response
        if entry.get() in a_dict:
            # Label(a_dict[entry.get()]).pack()
            entry_text = StringVar()
            entry2 = Entry(new_win, width= 42, textvariable=entry_text)
            entry_text.set(a_dict[entry.get()])
            entry2.pack()
    
        else:
            print(entry.get(), 'is not found in dictionary')


    Label(new_win, text="What is your emergency?").pack()
    Button(new_win, text="Check with dictionary", command=get_data).pack()
    #Create an Entry Widget
    entry = Entry(new_win, width= 42)
    entry.pack()


def get_dict():
    return {'bleeding': 'Cover the wound with sterile gauze or a clean cloth.', 
'breathing difficulties': 'Check the persons airway, breathing, and pulse and loosen any tight clothing.', 
'someone collapses': 'Loosen belts, collars or other constrictive clothing.', 
'fit or epißleptic seizure': 'Cushion their head if they\'re on the ground and loosen any tight clothing around their neck, such as a collar or tie, to aid breathing then turn them to thier side.', 
'severe pain': 'Get some gentle exercise or Breathe right to ease pain.', 
'heart attack': 'Chew and swallow an aspirin while waiting for emergency help or Begin CPR if the person is unconscious.', 
'a stroke': 'Call 911 and perform CPR.'}

#Initialize tkinter

root.title("Code fest health bot")

#Aarav place background pic


#Create function for emergency 

def chronic():
    #Create a new window
    new_win= Toplevel(root)
    new_win.title("Health bot emergency stage")

    #Create input field and match with dictionary 
    a_dict = {'bleeding': 'Cover the wound with sterile gauze or a clean cloth.', 
'breathing difficulties': 'Check the persons airway, breathing, and pulse and loosen any tight clothing.', 
'collpase': 'Loosen belts, collars or other constrictive clothing.', 
'fit' or 'epileptic seizure': 'Cushion their head if they\'re on the ground and loosen any tight clothing around their neck, such as a collar or tie, to aid breathing then turn them to thier side.', 
'severe pain': 'Get some gentle exercise or Breathe right to ease pain.', 
'heart attack': 'Chew and swallow an aspirin while waiting for emergency help or Begin CPR if the person is unconscious.', 
'stroke': 'Call 911 and perform CPR.'}



    # Define a function to return the Input data
    def get_data():
        
        #Check if key in dictioary and print response
        if entry.get() in a_dict:
            # Label(a_dict[entry.get()]).pack()
            entry_text = StringVar()
            entry2 = Entry(new_win, width= 42, textvariable=entry_text)
            entry_text.set(a_dict[entry.get()])
            entry2.pack()
    
        else:
            print(entry.get(), 'is not found in dictionary')


    Label(new_win, text="What is your emergency?").pack()
    Button(new_win, text="Check with dictionary", command=get_data).pack()
    #Create an Entry Widget
    entry = Entry(new_win, width= 42)
    entry.pack()


def get_dict():
    return {'Allergies': 'Over-the-counter (OTC) antihistamines and decongestants may relieve minor symptoms of an allergic reaction.', 
'Cold': 'Stay hydrated. Water, juice, clear broth or warm lemon water with honey helps loosen congestion and prevents dehydration, rest your body, try honey and add some moisture to the air', 
'Flu': 'Stay at home and rest and Avoid close contact with well people in your house so you wont make them sick.', 
'Conjunctivitis': 'You can use cold compresses and artificial tears, which you can purchase over the counter without a prescription.', 
'Diarrhea': 'Drink plenty of liquids, including water, broths and juices. Avoid caffeine and alcohol. Add semisolid and low-fiber foods gradually as your bowel movements return to normal.', 
'Headache': 'Rest in a quiet, dark room and Hot or cold compresses to your head or neck and Massage and small amounts of caffeine.', 
'Mononucleosis': 'Treatment mainly involves taking care of yourself, such as getting enough rest, eating a healthy diet and drinking plenty of fluids.', 
'Stomach Aches': 'Drinking water. Avoiding lying down. Ginger. BRAT diet. Avoiding smoking and drinking alcohol. Avoiding difficult-to-digest foods. Lime or lemon juice, baking soda, and water.'}






   

#Create chronic function
def chronic():
        #Create a new window
    new_win= Toplevel(root)
    new_win.title("Health bot emergency stage")

    #Create input field and match with dictionary 
    p_dict = {'Allergies': 'Over-the-counter (OTC) antihistamines and decongestants may relieve minor symptoms of an allergic reaction.', 
'Cold': 'Stay hydrated. Water, juice, clear broth or warm lemon water with honey helps loosen congestion and prevents dehydration, rest your body, try honey and add some moisture to the air', 
'Flu': 'Stay at home and rest and Avoid close contact with well people in your house so you wont make them sick.', 
'Conjunctivitis': 'You can use cold compresses and artificial tears, which you can purchase over the counter without a prescription.', 
'Diarrhea': 'Drink plenty of liquids, including water, broths and juices. Avoid caffeine and alcohol. Add semisolid and low-fiber foods gradually as your bowel movements return to normal.', 
'Headache': 'Rest in a quiet, dark room and Hot or cold compresses to your head or neck and Massage and small amounts of caffeine.', 
'Mononucleosis': 'Treatment mainly involves taking care of yourself, such as getting enough rest, eating a healthy diet and drinking plenty of fluids.', 
'Stomach Aches': 'Drinking water. Avoiding lying down. Ginger. BRAT diet. Avoiding smoking and drinking alcohol. Avoiding difficult-to-digest foods. Lime or lemon juice, baking soda, and water.'}



    # Define a function to return the Input data
    def get_data():
        
        #Check if key in dictioary and print response
        if entry.get() in p_dict:
            # Label(a_dict[entry.get()]).pack()
            entry_text = StringVar()
            entry2 = Entry(new_win, width= 42, textvariable=entry_text)
            entry_text.set(p_dict[entry.get()])
            entry2.pack()
    
        else:
            print(entry.get(), 'is not found in dictionary')


    Label(new_win, text="What is your emergency?").pack()
    Button(new_win, text="Check with dictionary", command=get_data).pack()
    #Create an Entry Widget
    entry = Entry(new_win, width= 42)
    entry.pack()




    

root.mainloop()