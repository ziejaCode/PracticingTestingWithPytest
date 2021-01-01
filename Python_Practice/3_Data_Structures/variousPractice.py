'''
Created on 22 Dec 2019
@author: M.Laptop
'''
#from builtins import False

lista1 = []




#print(lista1)
#print(len(lista1))


class Colection:    

    def __init__(self):        
        ''' this is how you create list with fixed size and fill it with one value 
            it is null in this case
        '''       
        self._sizik = 4
        self._table = [None] * self._sizik
    
    def _getHash(self, key):
        ''' This is hash function. It crates hash by
            taking ASCII number for each char in key
            and sum the taking reminder of it
        '''
        hash = 0
        for char in str(key):
            hash += ord(char)
            #print(hash)
        hash = hash % self._sizik
        #print(hash)
        return hash
     
    ''' this method will add new value to hashTable '''
    def addItem(self, key, value):
        ''' new hash is generated '''
        key_hash = self._getHash(key)
        key_value = [key, value]
        
        ''' check if slot is not taken already '''
        print(self._table[key_hash])
        if self._table[key_hash] is None:
            self._table[key_hash] = list([key_value])
        else:
            for pair in self._table[key_hash]:
                #print("Juz cos jest")
                if pair[0] == key:
                    pair[1] = value
                    return True
            self._table[key_hash].append(key_value)        
        #print(self._table[key_hash])
        return key_hash
        
    def getItem(self, key):
        key_hash = self._getHash(key)
        if self._table[key_hash] is not None:
            for pair in self._table[key_hash]:
                if  pair[0] == key:
                    val = pair[1]
                    print( "this is requested value ", pair[1])
                    return val
                print( "There is no such value  ", key)
                return None    
                
    def delete(self, key):
        ''' new hash is generated '''
        key_hash = self._getHash(key)               
        ''' check if slot is not taken already '''
        #print(self._table[key_hash])
        if self._table[key_hash] is None:
            return False
        for i in range(len(self._table[key_hash])):
            print(key_hash, self._table[i])


        
        
    def printMe(self):
        print("--Phonebook--")
        for item in self._table:
            if item is not None:
                print(str(item))
                 
        
col = Colection()
#col[3] = "huj"
#if col == None:       
    #print(None, "is")  
#else:
    #print(None, "is Not")
    
#col._getHash("45")    

col.addItem(54, "Marina")
print(col._table)
col.addItem(35, "Wiesia")
print(col._table)
col.addItem(34, "Frania")
print(col._table)
col.addItem(344, "Marina")
print(col._table)
col.addItem(15, "Wiesia")
print(col._table)
col.addItem(347, "Ziuta")
print(col._table)

col.getItem(15)
col.getItem(10) 

print()

col.delete(15)

print()    
#print(col._table)
print(col._sizik)

print()

col.printMe()






















