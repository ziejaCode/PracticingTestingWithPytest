'''
Created on 13 Sep 2020

@author: czarny
'''

import functools 

print(max(3,4,7,34, 5))

# can take list as argument
l = [3,4,7,34, 5, -1, 0]
print(max(l))



print(min([5, 8, 6, 10, 9]))
m = 4,
print(max([5, 8, 6, 10, 9]))

a,b = 4,5
print(list(map(lambda a, b: a+b, l,l)))

print(sum([5, 8, 6, 10, 9]))

l = [0, '', None, 100]

print(any(l))

print(all(l))

print(list(range(1, 7)) )

m = 5
print(functools.reduce(lambda a, b: a * b, range(1, m + 1)))


