#Create the dictionary for chronic
p_dict = {'Allergies': 'Over-the-counter (OTC) antihistamines and decongestants may relieve minor symptoms of an allergic reaction.', 
'Cold': 'Stay hydrated. Water, juice, clear broth or warm lemon water with honey helps loosen congestion and prevents dehydration, rest your body, try honey and add some moisture to the air', 
'Flu': 'Stay at home and rest and Avoid close contact with well people in your house so you wont make them sick.', 
'Conjunctivitis': 'You can use cold compresses and artificial tears, which you can purchase over the counter without a prescription.', 
'Diarrhea': 'Drink plenty of liquids, including water, broths and juices. Avoid caffeine and alcohol. Add semisolid and low-fiber foods gradually as your bowel movements return to normal.', 
'Headaches': 'Rest in a quiet, dark room and Hot or cold compresses to your head or neck and Massage and small amounts of caffeine.', 
'Mononucleosis': 'Treatment mainly involves taking care of yourself, such as getting enough rest, eating a healthy diet and drinking plenty of fluids.', 
'Stomach Aches': 'Drinking water. Avoiding lying down. Ginger. BRAT diet. Avoiding smoking and drinking alcohol. Avoiding difficult-to-digest foods. Lime or lemon juice, baking soda, and water.'}
#Make key
key = input('What is your issue? [type in all lower case or use text to speech]: ')
#Check if key is in dictionary
if key in p_dict:
    print(p_dict[key])

else:
    print(key, 'is not found in dictionary')