class Car:
    body = 'estate'
    brand = 'audi'

    def start():
        pass

print(Car.start)
print(Car.__name__)

print(Car.body)

Car.body = 'combi'
print(Car.body)

print(getattr(Car, 'body'))

setattr(Car, 'body', 'suv')

print(getattr(Car, 'body'))

# setting atribute
setattr(Car, 'engine', '10000cc')

print(getattr(Car, 'engine'))


Car.engine = '200cc'
print(getattr(Car, 'engine'))

print(type(Car.__dict__))

print(Car.__dict__)



# how to delete atribute 
delattr(Car, 'engine')
print(Car.__dict__)

print('\n\n')

print(list(Car.__dict__.items()))
for k in list(Car.__dict__.items()):
    print(k)