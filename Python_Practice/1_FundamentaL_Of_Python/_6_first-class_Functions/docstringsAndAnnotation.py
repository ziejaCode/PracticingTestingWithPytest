'''
Created on 1 Jun 2020

@author: czarn
'''
#from Cython.Includes.cpython import int

''' docstrings example '''


def myDocstring(a):
    "this is one hell of a docstring"
    return a

# this is how to use docstring 
help(myDocstring)

''' this method - __doc__  stores metadata string '''
#print(myDocstring.__doc__) 


''' Annotation methods '''

def my_func(a: 'a string', b: 'a positive integer') -> 'a string':
    " returns a * b and else"
    return a * b

print(my_func("2", 3))

help(my_func)

''' this method - __annotations__  stores metadata string '''
#print(my_func.__annotations__)
#print(my_func.__doc__)
#print(help(type))



def my_func(a: str, b: 'int > 0') -> str:
    return a,b


help(my_func)

a = [54,67,78]
print(my_func("45", a))




















