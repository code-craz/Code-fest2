myDict = {"name": "PythonForBeginners", "acronym": "PFB"}
print("Original Dictionary is:", myDict)
emn= input("What is the name of your emergency? : ")
ems= input("What is the solution to your issue? : ")
print(emn)
print(ems)
myDict[emn] = ems
print("Modified Dictionary is:", myDict)