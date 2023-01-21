a_dict = {'Bleeding': 'Solution', 'b': 200, 'c': 300}
key = input('what key: ')

if key in a_dict :
    print (a_dict[key])
else :
    print (key, 'is not found in the dictionary')