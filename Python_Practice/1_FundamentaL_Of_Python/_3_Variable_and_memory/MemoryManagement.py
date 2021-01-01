'''
Created on 12 Sep 2020

@author: czarny
'''

import sys
import ctypes
# this is how to find memory address of the variable
my_var1 = 34

my_var2 = "feef"

print(id(my_var2))

a,b,c,d = my_var2

t = a,b,c,d

print(a,b,c,d)

for i in t:
    print(id(i))
    
print(sys.getrefcount(my_var1))


#print(ctypes.c_long.from_address(sys.getrefcount(my_var1)).value)


# function and classes has addresses also 

def getMyVar1():
    pass



def getMyVar2():
    pass


print("This is ",id(getMyVar1))

print("This is ",id(getMyVar2))


print("check classes")

class MyClass:
    # asfjlskdjfsladjf
    pass

   
    
print("Class ", id(MyClass))
























