from Pion import *

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
            self.positionArray.append(pions.position)
    
    def getPionPosition(self):
        self.positionArray.clear()
        for pions in self.pionArray:
            self.positionArray.append(pions.position)
        return self.positionArray
    
    def evaluate(self):
        result = 0
        for pions in self.pionArray:
            result += (pions.maxpos-pions.position)
        return result
        

test = FactoryFunction()
newarray = Player()
print(newarray.evaluate())





