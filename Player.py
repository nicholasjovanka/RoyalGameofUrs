from Utils import *
from Pion import *

class PlayerClass:
    identifier = "Uninitialized"
    pionArray = []
    positionArray = []
    # alt solution, seperate pionArray to active, inactive, finished
    
    def __init__(self, identifier):
        self.pionArray = self.FactoryFunction()
        for pions in self.pionArray:
            self.positionArray.append(pions.position)

        self.identifier = identifier

    def FactoryFunction(self):
        pionArray = []
        for x in range(7):
            pion = PionClass()
            pionArray.append(pion)
        return pionArray
    
    def getPionPosition(self):
        self.positionArray.clear()
        for pions in self.pionArray:
            self.positionArray.append(pions.position)
        return self.positionArray.copy()
    
    def evaluate(self):
        result = 0
        for pions in self.pionArray:
            result += (pions.maxpos-pions.position)
        return result
