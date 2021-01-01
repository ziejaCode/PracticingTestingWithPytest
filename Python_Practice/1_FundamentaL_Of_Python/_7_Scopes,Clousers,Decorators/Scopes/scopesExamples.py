
# global scope
a = 10
n = 2

def myfunc(n):
    # local scope 
    global a   
    a = 2   
    return n * a

print(a)

print(myfunc(n))

print(a)

print('\n---break----\n')
# crateing and settint global in myfunc1

def myfunc1(n):
    # local scope 
    global b   
    b = 11  
    return n * b

# print(b)

print(myfunc1(n))

print(b)

print('\n---break----\n')


# referenced before assignment
f = 78
def myfunc2():
    # local scope 
    print("global ", f)   
    #f = 11  
    
myfunc2()