

class Person:
    pass


class School:
    pass

print(type(Person))

print(type(type))

print(Person.__name__)
print(Person.__init__)
print(Person.__dir__)
print(Person.__name__)

print("\n----------break----------\n")
# class as value

p = Person
print(p)
print(type(p))


r = Person()
print(r)
print(type(r))


print(isinstance(p, Person))
print(isinstance(r, Person))


print(help(type))