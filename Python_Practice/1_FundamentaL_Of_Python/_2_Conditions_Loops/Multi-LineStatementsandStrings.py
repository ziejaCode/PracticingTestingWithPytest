'''
Created on 26 Dec 2019
@author: M.Laptop
'''
#Multi-Line Statements and Strings

#Implicit Examples

a = [1, 
    2, 
    3]

a = [1, #first element
    2, #second element
    3, #third element
    ]

a = (1, # first element
    2, #second element
    3, #third element
    )

a = {'key1': 'value1', #comment,
     'key2': #comment
     'value2' #comment
    }



print(a)

def my_func(a, #some comment
           b, c):
    print(a, b, c)
    

my_func(10, #comment
       20, #comment
       30)


# Explicit Examples

a = 10
b = 20
c = 30
if a > 5 \
    and b > 10 \
    and c > 20:
    print('yes!!')


#Multi-Line Strings

a = '''this is
a multi-line string'''
    
b = """some items:
    1. item 1
    2. item 2"""
    
c = '''some items:\n
    1. item 1
    2. item 2'''
    
print(a, c)
    
def my_func():
    a = '''a multi-line string
    that is actually indented in the second line'''
    return a












