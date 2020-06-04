#!/usr/bin/env python
# coding: utf-8

# In[44]:


class Pion:
    position : int
    safe : bool
    finish : bool
    minpos = 0
    maxpos = 15
        
    def __init__(self):
        self.position = 0
    
    def getPosition(self):
        return self.position
    
    def setPosition(updatedPosition):
        self.position = updatedPosition
    
    def isSafe(self):
        return self.safe
    
    def isFinished(self):
        return self.finish
    
    def setSafe(newstate):
        self.safe = newstate
    
    def setSafe(newstate):
        self.finish = newstate    
    
    def getMaxPos(self):
        return self.maxpos
    
    def getMinPos(self):
        return self.minpos
    

def FactoryFunction():
    pionArray = []
    for x in range(7):
        pion = Pion()
        pionArray.append(pion)
    return pionArray

class Player:
    pionArray = []
    positionArray = []
    
    def __init__(self):
        self.pionArray = FactoryFunction()
        for pions in self.pionArray:
            self.positionArray.append(pions.getPosition())
    
    def getPionPosition(self):
        self.positionArray.clear()
        for pions in self.pionArray:
            self.positionArray.append(pions.getPosition())
        return self.positionArray
    
    def evaluate(self):
        result = 0
        for pions in self.pionArray:
            result += (pions.maxpos-pions.position)
        return result
        

test = FactoryFunction()
newarray = Player()
print(newarray.evaluate())


# In[ ]:




