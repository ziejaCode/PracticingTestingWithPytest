'''
Created on 11 Apr 2020

@author: czarn
'''
dicts = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

dicts = dict([(34,"sdfs"), (45, "fgdfgd")])

print(dicts.keys())
print(dicts.values())
print(dicts.items())

print(len(dir(dicts)))

for alfa, beta in dicts.items():
    print(alfa, " is ", beta)