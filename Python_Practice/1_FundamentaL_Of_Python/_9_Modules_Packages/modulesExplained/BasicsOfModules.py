# built-in library.py

#print('Running imports.py  - module name: {0}'.format(BasicsOfModules.__name__))
import math
print(math)

# BasicsOfModules.py
# standard library 
import numpy
print(numpy)

import sys


print(sys.modules)
print("@",math.__dict__['pow'])

import types

mod = types.ModuleType('test','This is a module')

print(type(mod))

mod.pi = 67

mod.myMod = lambda: 'I am mod'

print(mod.__dict__)

print('myMod' in globals()) 

myMod = mod.myMod

print('myMod' in globals())

print('mod' in globals())

print(dir(mod))















