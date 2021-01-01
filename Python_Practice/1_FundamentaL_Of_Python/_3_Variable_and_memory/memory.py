
import ctypes
x = 23
# this is how to get value from memory address
print(ctypes.cast(id(x),ctypes.py_object).value)
print(type(id(x)))
print(type(ctypes.cast(id(x),ctypes.py_object).value))


def outerFunc():        
    x = 'hello'  
    address = int( hex(id(x)), 16  )
    print(address)  
    def innerFunc():
        y = x        
        print(hex(id(y)))
    # return memory address 
    return address
    

fn = outerFunc()

import ctypes

# convert back to value
print(ctypes.cast(outerFunc(),ctypes.py_object).value)