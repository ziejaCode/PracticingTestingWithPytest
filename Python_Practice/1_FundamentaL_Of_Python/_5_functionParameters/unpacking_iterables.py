'''
Created on 26 Apr 2020

@author: czarn
'''

a = (1,2,3) # one way of createing a tuple


b = 1,2,3

print(type(a))
print(type(b))

'''
above shows that to create tuple you don,t need parentheses but commas 
'''

c = 1, # this is tuple as well

print(type(c))

# empty tuple
e = ()
print(type(e))

''' unpacking is also called parallel  assignment'''

a,b,c = [1,2,3]

print(a)
print(b)
print(c)


a,b,c = 34, 45.78, "toup toup"

print(a)
print(b)
print(c)

'''  
   reason we use unpacking is swaping one value for another without 
   
   temporary value for storage   
   
'''

''' more examples of swapping '''

a, b = 23, 34
print(a, b)
print(id(a))
print(id(b))

b,a = a,b
print(a,b)
print(id(a))
print(id(b))

l = [23, 45,78]

a,b,c = l

print(a, b, c)

c,a = b,c

print(a, b, c)


''' unpacking set is not very useful'''

s = {'m', 'a','r','i'}

a,b,c,d = s

print(a,b,c,d)

''' unpacking dictionaries is not very useful 
        because order is not warranted
'''

d = {'a':23,'b':45,'c':56,'d':12}
print(d)
a,b,c,d = d
print(a,b,c,d)
print(d)

v = {'a':23,'b':45,'c':56,'d':12}

a,b,c,d = v.values()
print(a,b,c,d)

a,b,c,d = v.items()
print(a,b,c,d)

''' Extended unpacking '''

l = [1, 2, 3, 4, 5, 6]

a,b = l[0],l[1:]
print(a)
print(b)
print("---------")
*a,b,c = l 

print(a)
print(b)
print(c)

print("---------")
a,b,*c = l 

print(a)
print(b)
print(c)

print("---------")
a,*b,c = l 

print(a)
print(b)
print(c)

''' Star arguments may be userd in many ways 
    Below they combine different arrays of data
'''

l = {23,34,56,78,90}
la = [{23,34,56,78,90},{23,34,56,78,90},{23,34,56,78,90}]


print(*l, *la)


'''  below all keys from three dict are put in one list and set '''

d1 = {'p': 1, 'y': 2}
d2 = {'t': 3, 'h': 4}
d3 = {'h': 5, 'o': 6, 'n': 7}


l = [*d1, *d2, *d3]
print(l)

l = {*d1, *d2, *d3}
print(l)


d1 = {'p', 'y'}
d2 = {'t', 'h'}
d3 = {'h', 'o' ,'n'}


l = [*d1, *d2, *d3]
print(l)



''' Using ** operator we can extract both key and value 
    below all keys and values from three dicts are put in one list and set '''


d1 = {'p': 1, 'y': 2}
d2 = {'t': 3, 'h': 4}
d3 = {'h': 5, 'o': 6, 'n': 7} 

d = {**d1, **d2, **d3}

print(d)

''' nested unpacking '''
l = [[1,2],3,[4,5]]
var = "<class 'list'>"
print(var)
#(a,b),c,(d, e)= l

(a, b),c,(d,e) = l

b = [a,b,c,d,e]

print(b)

print("------------")

b = []
for i in l:
    if isinstance(i, list):
        for j in i:
            b.append(j)
    else:
        b.append(i) 

print(b)

''' for the above code apply abstraction '''



















