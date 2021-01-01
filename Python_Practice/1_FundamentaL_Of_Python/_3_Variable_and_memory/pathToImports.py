'''
Created on 9 Apr 2020

@author: Marty
'''
import sys

def pinSysDirect12():
    # shows where is python installed
    #print('\n',sys.prefix)
    return ('\n',sys.prefix)

def pinSysDirect22():
    # where are compiled binaries are stored
    #print('\n',sys.exec_prefix)
    return ('\n',sys.exec_prefix)


print(pinSysDirect22()) 