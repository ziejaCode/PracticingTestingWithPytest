'''
Created on 26 Dec 2019

@author: M.Laptop
'''
# these are ternary operators
i = 3
x = '4' if i < 5 else '7'
print(x)

def say_hello():
    print('Hello!')
    
def say_goodbye():
    print('Goodbye!')
    
a = 5
say_hello() if a < 10 else say_goodbye()