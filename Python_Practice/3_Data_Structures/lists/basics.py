'''
Created on 11 Apr 2020

@author: czarn
'''

l = [3, 4, 5, 'w', 'erer', 45.6, 67]

print(l[2])
print(len(l))

# slicing lists   

print(l[4:])  # all from 4th element   

print(l[:-1]) # fetch all elements except the last

print(4 in l)

print(4 not in l)

i = None 
print(type(i))
print(type(34.5))
print(type(23))

import sys as s
print(type(s))



methodsList = dir(l) # dir method extract all method from given variable

print(len(methodsList))

for ml in methodsList:
    print(ml)



[2,3,4].





 