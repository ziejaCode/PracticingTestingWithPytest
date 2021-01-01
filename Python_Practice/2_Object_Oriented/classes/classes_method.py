# in this module I will show how to add attributes to class at the runtime

class Produkt:
    def ref_num(self):
        print(f'Prod num is: {self}')


print('This is ', hex(id(Produkt)))

p = Produkt()

p.ref_num()

print(hex(id(p)))

#print(p.ref_num())
#print(p.__dict__)
#print(Produkt.__dict__)

# here we add function at runtime

Produkt.price = lambda self: f'price is {self}'
print(p.__dict__)
#print(Produkt.__dict__)

print(p.price)

print(Produkt.price(p))

p.avaiability = lambda : 'Its on stock'

print(p.avaiability)

# how to add functio as metod to class instance
print('\n------------- break -----------\n') 


class Person():
     def __init__(self, name):
         self.name = name

p1 = Person('Norman')
p2 = Person('Herman')

print(p1)
print(p2)
print(Person.__dict__)
print(p1.__dict__, p2.__dict__)

# here is some funtion
def say_hello(self):
    return f'{self.name} says hello'

print(say_hello(p1))


Person.say = say_hello

print(Person.__dict__)

print(Person.say)
print(say_hello)