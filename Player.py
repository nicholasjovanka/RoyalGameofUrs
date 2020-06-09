from Utils import *
from Pion import *

class PlayerClass:
    name = ""
    identifier = "" #format: [Player (1/2) (int), "Human"/"Bot"]
    pionArray = []
    positionArray = []
    # alt solution, seperate pionArray to active, inactive, finished
    
    def __init__(self, name, identifier):
        self.pionArray = self.FactoryFunction(identifier[0])
        for pions in self.pionArray:
            self.positionArray.append(pions.position)

        self.name = name
        self.identifier = identifier

    def FactoryFunction(self, playerIdentifier):
        pionArray = []
        if playerIdentifier == 1:
            for x in ['1', '2', '3', '4', '5', '6', '7']:
                pion = PionClass(x)
                pionArray.append(pion)

        elif playerIdentifier == 2:
            for x in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
                pion = PionClass(x)
                pionArray.append(pion)

        return pionArray
    
    def getPionPosition(self):
        self.positionArray.clear()
        for pions in self.pionArray:
            self.positionArray.append([pions.position, pions.identifier])
        return self.positionArray.copy()
    
    def evaluate(self, positionArray):
        result = 0
        for pions in positionArray:
            result += 15-pions
        return result

