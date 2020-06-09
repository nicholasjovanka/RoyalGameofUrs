from Utils import *
from Pion import *

class PlayerClass:
    name = ""
    identifier = "" #format: [Player (1/2) (int), "Human"/"Bot"]
    pionArray = []
    positionArray = []
    # alt solution, seperate pionArray to active, inactive, finished
    
    def __init__(self, name, identifier, initialPionPosition= None):
        if initialPionPosition == None:
            self.pionArray = self.FactoryFunction(identifier[0])
        else:
            self.pionArray = self.FactoryFunction(identifier[0], initialPionPosition)

        for pions in self.pionArray:
            self.positionArray.append(pions.position)

        self.name = name
        self.identifier = identifier

    def FactoryFunction(self, playerIdentifier, initialPionPosition= None):
        pionArray = []
        identifierArray = []
        if playerIdentifier == 1:
            identifierArray = ['1', '2', '3', '4', '5', '6', '7']
        elif playerIdentifier == 2:
            identifierArray = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

        for x in range(len(identifierArray)):
            if initialPionPosition == None:
                pion = PionClass(identifierArray[x])
            else:
                pion = PionClass(identifierArray[x], initialPionPosition[x])
            pionArray.append(pion)

        return pionArray
    
    def getPionPosition(self):
        self.positionArray.clear()
        for pions in self.pionArray:
            self.positionArray.append([pions.position, pions.identifier])
        return self.positionArray.copy()

    def testPionPosition(self):
        self.positionArray.clear()
        for pions in self.pionArray:
            self.positionArray.append([pions.position, pions.identifier])
        return self.positionArray.copy()
    
    def evaluate(self, positionArray):
        result = 0
        for pions in positionArray:
            result += 15-pions
        return result

