'''
Created on 26 Dec 2019
@author: M.Laptop
'''

# Lambdas


from datetime import date, timedelta

#number of weeks to end of the year
def numOfWeeksLeft1():
    return 53 - date.today().isocalendar()[1]


#number of weeks to end of the year LAMBDA
numOfWeeksLeft = lambda x = 53:  x - date.today().isocalendar()[1]


print(186 * numOfWeeksLeft())


funk1 = lambda x = 4: x**3


print(funk1())


