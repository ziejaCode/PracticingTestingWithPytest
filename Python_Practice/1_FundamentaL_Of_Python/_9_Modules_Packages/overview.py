
'''
def func():
    return 10

print(func)
print(func())
f = globals()['func']
print("\n",f)
l = locals()['func']
print(f)
print(l)
print(f is l)


import math

print(id(math))

print(type(math))
print(type(34))

print(globals()['math']) 

import sys
print(id(sys.modules['math']))
print(type(math))
fraction = math

# print(math.__dict__)
math.__dict__

import calendar

print(calendar)

import types
print(type(types))
# print(types.__all__)
'''


