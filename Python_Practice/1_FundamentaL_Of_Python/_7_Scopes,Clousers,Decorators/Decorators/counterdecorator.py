def counter(fn):
    count = 0
    print(hex(id(count)))
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print('Function {0} (id({1})) was called {2} times'.format(fn.__name__, id(fn), count))
        return fn(*args, **kwargs)
    
    return inner

def add(a: int, b:int = 0):
    """
    adds two values
    """
    return a + b

help(add)
print(id(add))
print((add.__closure__))
print(add.__code__.co_freevars)

print('\n---------break------------\n')

add = counter(add)

help(add)
print(id(add))
print((add.__closure__))
print(add.__code__.co_freevars)


add(10, 20)

add(10, 20)

print('\n---------break 2 ------------\n')

@counter
def myfunc(s:str, i:int) -> str:
    return s * i

#myfunc = counter(myfunc)
print(myfunc('e', 6))