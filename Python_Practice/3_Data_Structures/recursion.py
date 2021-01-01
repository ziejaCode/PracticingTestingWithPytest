'''
Created on 21 Dec 2019

@author: M.Laptop
'''
def sum(list):
  if list == []:
    return 0
  return list[0] + sum(list[1:])


def fact(x):
  if x == 1:
    return 1
  else:
    return x * fact(x-1)

print( fact(5))

'''  '''

def countdown(i):  
  # base case
  if i <= 0:
     return
  # recursive case
  else:
     print(i)
     countdown(i-1)

countdown(5)


'''  '''

def greet2(name):
    print("how are you, " + name + "?")

def bye():
    print ("ok bye!")

def greet(name):
    print("hello, " + name + "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()

greet("adit")




















