'''
Created on 16 Sep 2020

@author: czarny
'''
import sys

print(sys.prefix)

libs = sys.path

for l in libs:
    print(l)