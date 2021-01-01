# this module is used to read other modules objects

a = ['audi','justCar','volovo']
c = 'tralala'
def print_classes(mod):
        x = dir(mod)
        l = []
        for obj in x:
            print(obj)
            l.append(obj)
        return l

class classieClass:
    b = 'jestem classa :) '