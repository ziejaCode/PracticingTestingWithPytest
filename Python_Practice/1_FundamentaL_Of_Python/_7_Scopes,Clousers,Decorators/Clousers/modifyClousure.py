
def outer():
    count = 0
    def inc1():
        nonlocal count
        count += 1
        return count
    def inc2():
        nonlocal count
        count += 1
        return count
    return inc1, inc2

fn1, fn2 = outer()
print(fn1.__code__.co_freevars, fn2.__code__.co_freevars)
# value address
print(fn1.__closure__, fn2.__closure__)
# modify address
fn1()
print(fn1.__closure__, fn2.__closure__)
# modify address
fn2()
print(fn1.__closure__, fn2.__closure__)



print('\n-------break--------\n') 
# another example

def pow(n):
    def inner(x):
        return x ** n
    return inner

square = pow(3)

print(square(2))
