'''
Created on 19 Apr 2020
Explanation and practice of positional and keyword arguments
@author: czarn
'''

''' positional arguments '''
def my_func(a,b,c):
    print("a={0}, b={1}, c={2}".format(a, b, c))

my_func(2, 13, 5) # all arguments must be called

# or - use default arguments
def my_func1(a,b=12,c=50): # second argument is default so all following must be default as well
    print("a={0}, b={1}, c={2}".format(a, b, c))

my_func1(2, 33, 15) # if you call this way default value is replaced

my_func1(2) # in this case only non default argument is called

''' named arguments '''
# same method call but arguments are named
my_func1(a=23, b=73, c=45) 

# how it is called
my_func()

# when arguments are named the position doesn't matter
my_func1(b=23, a=73, c=45)

# default still doesn't have to be called
my_func1(b=23, a=73)


# positional and keyword can be mixed and matched 
my_func1(23, c=73, b=45)



''' Mandatory keyword parameters '''


# positional and keyword can be mixed and matched 
my_func1(23, c=73, b=345)
#>>>>>>> branch 'master' of https://github.com/czarny25/pythonStudy.git




