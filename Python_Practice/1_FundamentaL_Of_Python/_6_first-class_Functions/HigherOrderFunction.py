'''
Created on 6 Jun 2020

@author: czarn
'''



l1 = [1, 2, 3]
l2 = [10, 20, 30, 40]
print(l1, l2)

"Map function"
print(list(map(lambda x, y, z: x + y , [1, 2, 3], [10, 20, 30], [10, 20, 30])) )

"Fileter function"
print(list(filter(lambda n: n % 2 == 0, l1)) )

"zip function"
print(list(zip(l1, l2)) )

"List comprehension - this is just short way to process list elements"
print([x**2 for x in l1])
print([x**2 for x in [10, 20, 30, 40]])

"map comprehension - this is just short way to process map elements"
print([x + x for x, y in zip(l1, l2)])

"list filter comprehension - this is just short way to process map elements"
[x for x in l1 if x % 2 == 0] 


"Combining map and filter"
print([x**2 for x in range(10) if x**2 < 25] )

