def value_swap(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner



def div1(a,b):
    print(a/b)

div1(2,4)



@value_swap
def div(a,b):
    print(a/b)

div(2,4)

print("\n-------break--------\n")

def pow(func):
    def inner(a):
        a = a ** 2
        print 
        return func(a)
    return inner

def piCalc(func):
    from math import pi
    def inner(a):
        a = a * pi
        return func(a)
    return inner

 

@pow
@piCalc
def computeArea(r):
    return r

print(computeArea(4))