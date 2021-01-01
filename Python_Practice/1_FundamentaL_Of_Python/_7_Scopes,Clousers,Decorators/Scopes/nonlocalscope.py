
def outfunc():
    x = 'hello'
    def infunc():
        print(x)
    return infunc()

#outfunc()

out = outfunc()

out

print('\n---break----\n')

x = 'python'
def outerFunc():
    #global x
    x = 'hello'
    print('outer', id(x), x)
    def innerFunc():
        #global x
        nonlocal x
        x = 'world'
        print('inner',id(x), x)
    print('outer',id(x), x)
    innerFunc()
    print('outer',id(x), x)

print('global',id(x), x)
outerFunc()
print('global',id(x), x)

import ctypes
print(ctypes.cast(id(x),ctypes.py_object).value)