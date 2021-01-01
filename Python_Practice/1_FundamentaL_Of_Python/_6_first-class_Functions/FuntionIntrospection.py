'''
Created on 6 Jun 2020

@author: czarn
'''
import inspect
#print(dir())

def test(a):
    return a + 3
print(dir(test))


print(test.__code__)

print(type(inspect))


def my_func():
    pass

class MyClass:
    def func(self):
        pass

    
my_obj = MyClass()

print(dir(inspect))
#func is bound to my_obj, an instance of MyClass

print(inspect.ismethod(my_func)) #→ False
print(inspect.isfunction(my_func)) #→ True'''
print(inspect.isroutine(my_func)) #→ False
print(inspect.isroutine(my_func))
print("--------------------------")
print(inspect.ismethod(my_obj.func)) #→ False
print(inspect.isfunction(my_obj.func)) #→ True'''
print(inspect.isroutine(my_obj.func)) #→ False
print(inspect.isroutine(my_obj.func))


a10 = 'fhfh'

print(a10)










