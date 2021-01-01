'''
Created on 21 Dec 2019
@author: M.Laptop
'''

from timeit import default_timer as timer

start = timer()
print(start)



def quicksort1(array):
    counter = 0
    if len(array) < 2:
        return array
    else:
        for i in range(int(len(array))):
            for i in range(1,len(array)):
                if array[i-1] > array[i]:
                    temp = array[i]
                    array[i] = array[i-1]
                    array[i-1] = temp
                    counter = counter + 1
    print(counter)
    return array


print (quicksort1([10, 5, 2, 3 , 6, 3, 10, 5, 2, 3 , 6, 3, 10, 5, 2, 3 , 6, 3]))

end = timer()

print(end)
print(end - start)

