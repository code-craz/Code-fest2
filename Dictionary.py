#Create a dictionary for emergency
a_dict = {'bleeding': 'Cover the wound with sterile gauze or a clean cloth.', 
'breathing difficulties': 'Check the persons airway, breathing, and pulse and loosen any tight clothing.', 
'someone collapses': 'Loosen belts, collars or other constrictive clothing.', 
'fit or epißleptic seizure': 'Cushion their head if theyre on the ground and loosen any tight clothing around their neck, such as a collar or tie, to aid breathing then turn them to thier side.', 
'severe pain': 'Get some gentle exercise or Breathe right to ease pain.', 
'heart attack': 'Chew and swallow an aspirin while waiting for emergency help or Begin CPR if the person is unconscious.', 
'a stroke': 'Call 911 and perform CPR.'}
#Get the input key for the dictionary
key = input('What is your emergency? [type in all lower case or use text to speech]: ')

#Check if key in dictioary and print response
if key in a_dict:
    print(a_dict[key])

else:
    print(key, 'is not found in dictionary')