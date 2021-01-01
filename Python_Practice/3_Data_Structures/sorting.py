'''
Created on 21 Dec 2019
@author: M.Laptop
'''
import pandas as pd

list = [2,4,5,2,15,6,4,6,8]

print(list[1:])
print(list[:2])


def count(list):
  if list == []:
    return 0
  return 1 + count(list[1:])
 

print(count(list)) 


  
def max(list):
  if len(list) == 2:
    return list[0] if list[0] > list[1] else list[1]
  sub_max = max(list[1:])
  print(max(list[1:]))
  return list[0] if list[0] > sub_max else sub_max


#print(max(list)) 

''' '''



def max1(list):
    
    maxNum = list[0] 
    
    for i in range(1,len(list)):
        if maxNum < list[i]:
            maxNum = list[i]
            print(list[i+1])       
    return maxNum

print("this is ", max1(list))


''' '''


def max2(list):    
    maxNum = list[0]     
    for i in range(1,len(list)):
        maxNum = list[i] if maxNum < list[i] else maxNum       
    return maxNum

print("this is ", max2(list))


''' '''

# Create the Timestamp object 
ts = pd.Timestamp(year = 2011,  month = 11, day = 21,  
                  hour = 10, second = 49, tz = 'US/Central')  
  
# Print the Timestamp object 
num1 = ts.timestamp()
print(num1)



def quicksort(array):
  if len(array) < 2:
    # base case, arrays with 0 or 1 element are already "sorted"
    return array
  else:
    # recursive case
    pivot = array[0]
    # sub-array of all the elements less than the pivot
    less = [i for i in array[1:] if i <= pivot]
    # sub-array of all the elements greater than the pivot
    greater = [i for i in array[1:] if i > pivot]
    print("nastepna runda")
    return quicksort(less) + [pivot] + quicksort(greater)

print (quicksort([10, 5, 2, 3]))

num2 = ts.timestamp()
print(num2) 
''' '''
print(num2 - num1)

def quicksort1(array):
  if len(array) < 2:
    return array
  #else: 























































