'''
This module present how to register various functions and bound it to various object so they 
can produce different output from calling the same method.
'''


from types import MethodType

class Person:
    def __init__(self, name):
        self.name = name

    def register_do_work(self, func):
        setattr(self, '_do_work', MethodType(func, self))

    def do_work(self):
        do_work_method = getattr(self, '_do_work', None)

        if do_work_method:
            return do_work_method()
        else:
            raise AttributeError('You must first register a do_work method')


math_teach = Person('Raf')
english_teach = Person('Monk')

def work_math(self):
    return f'{self.name} will teach adders toaday'

math_teach.register_do_work(work_math)

print(math_teach.__dict__)

print(math_teach.do_work())
