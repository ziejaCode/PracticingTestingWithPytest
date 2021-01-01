'''
Created on 1 Jun 2020

@author: czarn
'''
#from gevent.testing.monkey_test import kwargs

a, b, *c = 23, 34, 45, 23

print(a)
print(b)
print(c)
print("---------------")

a, *b, c = 23, 34, 45, 23

print(a)
print(b)
print(c)

print("---------------")
*a, b = 23, 34, 45, 23
print(a)
print(b)
print(c)


print("---------------")
*a, b = 23, 34, 45, 23
print(a)
print(b)
print(c)


print(type(a))
print(b)

def makeList(*args):
    l = [args]
    return l

print(type(makeList(34,65,12,"fds")))


'''def makeDict(*args1, *args2): - this will not work
    #return args1 '''



def makeDict(d, *args):
    l = {d: args}
    return l

#print(type(makeList1(34,65,12,"fds", d= 34)))
#print("makeDict 1", makeDict(34,65,12,"fds", d=34))

g = [34,65,12,"fds"]
h = {43,56,786,43,787,343,'ghfjf'}

print("makeDict 2", makeDict("Marian", *g ))

print("makeDict 2", makeDict("Hela", *h ))



def makeDict1(d, *args):    
    return args

#print(type(makeList1(34,65,12,"fds", d= 34)))
print(makeDict1(34, 34,65,12,"fds"))


" **kwarks takes various amount of keyword arguments and turn them into a dictionary"

def func(d, **kwargs):
        return d, kwargs
    
print("make kwark",func("Roman", surname = "Marek", proffesion="stolarz"))


def func1(**kwa):
        return kwa
    
print("make kwa",func1(d=1,  name= "Roman", surname = "Marek", proffesion="stolarz"))


''' this method will take dict and update it for new items '''

def dodict(*args, **kwds):
    #print(type(args))
    d = {}
    for k, v in args: 
       d[k] = v 
       #print(d[k])
    d.update(kwds)
    return d 


#data = ("red" , "green" )

data = {"red":1 , "orange":2 , "green":34}
data1 = {"amber":2, "pink":4, "blue" :5}
print("---------------")
print(data1)
print(data)
print(data.update(data1))
print("---------------")
print(data1)
print(data)
print("---------------++++++++++")
data1.update(data)
print(data1)
print(data)
print("---------------")


tada = dodict(*data.items(),  *data1.items() ) 
print(tada)

tada = dodict(*data1.items(), a=43,b=45,c=56 ) 
print("tada", tada)




print("---------------")
print(data.update(data1))
print(data)

print("---------------")
print("---------------")
print("---------------")

''' this method will calculate the average of given elements '''

def calc_hi_lo_avg(*args, log_to_console=False):
    hi = int(bool(args)) and max(args)
    lo = int(bool(args)) and min(args)
    avg = (hi + lo)/2
    if log_to_console:
        print("high={0}, low={1}, avg={2}".format(hi, lo, avg))
    return avg

print(calc_hi_lo_avg(23, 34, 45, 23))
print(int(calc_hi_lo_avg(23, 34, 45, 23 , log_to_console=True)))


''' default value use example  '''

from datetime import datetime

def log(msg1, *, dt=datetime.utcnow()): 
    print('{0}: {1}'.format(dt, msg1))    
    
log('message 1')    
    

def log1(msg, *, dt=None):
    dt = dt or datetime.utcnow()
    print('{0}: {1}'.format(dt, msg))        


#log('message 2')
log('message 2', dt="2020-06-01 15:00:46")













