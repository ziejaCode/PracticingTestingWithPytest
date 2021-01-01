'''
Created on 26 Dec 2019

@author: M.Laptop
'''

# while loops
'''
min_length = 2

name = input('Please enter your name:')

while not(len(name) >= min_length  and name.isprintable() and name.isalpha()):
    name = input('Please enter your name:')

#print('Hello, {0}'.format(name))min_length
'''

min_length = 2

while True:
    name = input('Please enter your name:')
    if len(name) >= min_length  and name.isprintable() and name.isalpha():
        break

print('Hello, {0}'.format(name))


# how to use else along with while

l = [1, 2, 3]
val = 10

idx = 0
while idx < len(l):
    if l[idx] == val:
        break
    idx += 1
else:
    l.append(val)

print(l)




''' ------------------ '''



a = 0
b = 5

while a < 3:
    print('-------------')
    a += 1
    b -= 1
    try:
        res = a / b
    except ZeroDivisionError:
        print('{0}, {1} - division by 0'.format(a, b))
        res = 0
        break
    finally:
        print('{0}, {1} - always executes'.format(a, b))
        
    print('{0}, {1} - main loop'.format(a, b))
else:
    print('\n\nno errors were encountered!')



''' ------------------ '''
    

a = 10
b = 1
try:
    a / b
except ZeroDivisionError:
    print('division by 0')
finally:
    print('this always executes')



''' --------  NOW FOR Loop ---------- '''

s = 'hello'

for i in enumerate(s):
    print("oto ", i)

''' ------------------ '''
 
 
#s = [2,3,5,6,7]   
    
print(s[3])
 
    
    
    
''' ------------------ '''
    
    
    
    
    
    
    
''' ------------------ '''













