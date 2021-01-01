'''
Created on 12 Sep 2020

@author: czarny
'''

my_var1 = 34
print(type(my_var1))

my_var1 = "var"
print(type(my_var1))

my_var2 = "this is string",
print(type(my_var2))

my_var1, my_var2 = my_var2, my_var1

print(type(my_var1))
print(type(my_var2))

my_var1 = [3,5,6]

my_var2 = my_var1

print(id(my_var1))
print(id(my_var2))

my_var1.append(7)
print(id(my_var1))

print(not(my_var1 is None))



print(id(my_var1[0]))
print(id(my_var2[0]))













