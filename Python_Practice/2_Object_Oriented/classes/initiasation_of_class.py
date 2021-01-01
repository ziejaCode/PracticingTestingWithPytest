
# init method is like constructor in Java

class Mamal:
    def __init__(self):
        print(f'Initializing a new mamal: {self}')


m = Mamal()

print(hex(id(m)))

# new constructor

class Plane:
    def __init__(self, type_): # more arguments 
        self.type_ = type_

p = Plane('Chopper')
print(p)