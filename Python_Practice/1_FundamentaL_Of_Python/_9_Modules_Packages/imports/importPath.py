'''
Created on 9 Apr 2020

@author: Marty
'''
import sys
import os

print('**********************************************************')
def pinSysDirect12():
    # shows where is python installed
    print('\n',sys.prefix)

pinSysDirect12()

print('**********************************************************')   

def pinSysDirect22():
    # where are compiled binaries are stored
    print('\n',sys.exec_prefix)

pinSysDirect22()

print('**********************************************************')

def showYourCurrentPath():
    # this will show your current path of this file
    print('\n',os.getcwd(),'\n\n')

showYourCurrentPath()


print('**********************************************************')
def showAllPath():
    for l in sys.path:
        print(l)
showAllPath()








