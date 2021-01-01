'''
Created on 9 Apr 2020

@author: Marty
'''
import sys
import os


def pinSysDirect12():
    # shows where is python installed
    print('Python installation\n',sys.prefix)
    

def pinSysDirect22():
    # where are compiled binaries are stored
    print('\n',sys.exec_prefix)
    


def showYourCurrentPath():
    # this will show your current path of this file
    print('\n',os.getcwd())



def showAllPath():
    for l in sys.path:
        print(l)

pinSysDirect12()

pinSysDirect22()

showYourCurrentPath()

print(" ") # just break

showAllPath()

import sqlalchemy

print(sqlalchemy.__version__)
