
import counter

@counter
def myf(s:str, i:int) -> str:
    return s * i

#myfunc = counter(myfunc)
print(myf('e', 6))