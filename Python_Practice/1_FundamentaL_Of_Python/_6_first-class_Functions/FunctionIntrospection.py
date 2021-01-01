'''
Created on 12 Sep 2020

@author: czarny
'''
import inspect as insp
from builtins import callable

def myFunc(x, s):
    w = dir(myFunc)    
    return w

myFunc("x", 3)

print(insp.isclass(myFunc("x", 3)))

myFunc.kategoria = 'kategoria testowa'

print(dir(myFunc))

print(insp.getmodule(myFunc) )

print(callable(myFunc))