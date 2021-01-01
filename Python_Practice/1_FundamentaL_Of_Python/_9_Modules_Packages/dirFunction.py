
def func():
    return"hey"

print(func)

print(func())

print(id(func))

print(globals())

g = globals()['func']

print(g is func)

