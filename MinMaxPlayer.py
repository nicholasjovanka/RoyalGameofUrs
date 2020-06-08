from GreedyPlayer import GreedyPlayerClass
import random

class MinMaxPlayerClass(GreedyPlayerClass):

    rosette = [4,8,16]

    def getChance(self, n):
        diceChance = [0.0625,0.25,0.375,0.25,0.0625]
        return diceChance[n]

    def evalBoard(self, enemyPos, selfPos, prefSelfPos):
        advDist = self.evaluate(enemyPos) - self.evaluate(selfPos)
        for i in range(len(selfPos)):
            if not (prefSelfPos[i][0] in self.rosette) and selfPos[i][0] in self.rosette:
                advDist += 2
        return advDist

    def simulateMovement(self, pos1,pos2):
        return

    # player = -1 => enemy, player = 1 => self
    def testMinMax(self, n, enemyPos: int, selfPos: int, player=1, iteration=3):
        if player == 1:
            if n > -1:
                oldPionPosition, currPionPosition = selfPos.copy()
                currPionPosition += n
                if not currPionPosition in self.rosette:
                    player *= -1
                if iteration > 0:
                    return self.testMinMax(-1, enemyPos, currPionPosition, player, iteration-1)
                else:
                    return self.evalBoard(enemyPos, currPionPosition, oldPionPosition)
            else:
                values = []
                for i in range(5):
                    oldPionPosition, currPionPosition = selfPos.copy()
                    currPionPosition += i
                    if not currPionPosition in self.rosette:
                        player *= -1
                    if iteration > 0:
                        values.append(self.testMinMax(i, enemyPos, currPionPosition, player, iteration-1))
                    else:
                        values.append(self.evalBoard(enemyPos, currPionPosition, oldPionPosition))
                return values.index(max(values))
        elif player == -1:
            return
            # TODO MAKE OPPONENT MOVE POSSIBLE
        
    def minmax(self, n, enemyPos, chance, player = 0, iteration = 3):
        value : float
        if player == 0:
            value = 0
            if(iteration <= 0):
                print("reached end")     
        elif player == 1:
            print("test")

        print("recursing", iteration)
        return value + self.minmax(n, enemyPos, iteration-1)
