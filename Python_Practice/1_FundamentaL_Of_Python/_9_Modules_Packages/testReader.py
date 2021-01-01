import readOtherModules, io, platform

# this is how to use imported module

print('\n it is working \n')
mod = platform
print(mod.__doc__)
objects = readOtherModules.print_classes(mod)
print(type(objects))

# get the list of the moduele's object and check its type

for obj in objects:
    print(obj, ' - type ', type(obj))
    pass

print(readOtherModules.a, ' and what is that ', type(readOtherModules.a))
print(readOtherModules.classieClass.b, ' and what is that now', type(readOtherModules.classieClass.b))

# where this module is stored
