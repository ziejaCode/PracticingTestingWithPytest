class Auto:
    marka = "volvo"
    def acelerate(self):
        #print(format("Start {0}", marka)
        print(f'brrr {Auto.marka}')



for k in list(Auto.__dict__):
    pass
    #print(k)

#print(Auto.acelerate , getattr(Auto, 'acelerate'))

#print(Auto.acelerate())

print(Auto.__dict__['acelerate']())


class Man:

    def say_Hello(self):
        print('hello')



#print(Man.say_Hello())

print("\n----------break----------\n")

# here it is how to change type of the particular class and object

class TestType:
    __class__ = str # this changes type of class to string

# class object
print(TestType.__class__)
print(type(TestType))
print(isinstance(TestType, type)) # gets tricked by name change

# instance object
tt = TestType()
print(tt.__class__)
print(type(tt))
print(isinstance(tt, str))