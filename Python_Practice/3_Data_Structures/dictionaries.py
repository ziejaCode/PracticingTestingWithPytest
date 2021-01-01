'''
Created on 21 Dec 2019
@author: M.Laptop
'''

book = dict()
# an apple costs 67 cents
book["apple"] = 0.67
# milk costs $1.49
book["milk"] = 1.49
book["avocado"] = 1.49
print (book)

'''  '''


voted = {}
def check_voter(name):
  if voted.get(name):
    print("kick them out!")
  else:
    voted[name] = True
    print("let them vote!")

check_voter("tom")
check_voter("mike")
check_voter("mike")

''' '''









