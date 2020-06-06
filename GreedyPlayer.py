from Utils import *
from Pion import *
from Player import *

class GreedyPlayerClass(PlayerClass):
    simulatedPions = []
    # simulatedPositions = []
    #
    # def simulatePositions(self):
    #     self.simulatedPions.clear()
    #     for pions in self.simulatedPions:
    #         self.simulatedPions.append(pions.position)
    #     return self.simulatedPions

    def bestPion(self,n : int, enemyPosition):
        best = 9999999
        chosenPion = 0
        for i in range(7):
            self.simulatedPions = self.pionArray.copy()
            canmove, nextTurn, eaten = self.simulatedPions[i].move(n,enemyPosition,self.getPionPosition())
            if(canmove):
                advantage = 0
                if(nextTurn == False):
                    advantage = -4
                evaluation = (self.simulatedPions[i].distanceToGoal() + self.simulatedPions[i].nextRosette()[1] - eaten + advantage)
                if evaluation < best:
                    best = evaluation
                    chosenPion = i
        return(chosenPion, best)
            
