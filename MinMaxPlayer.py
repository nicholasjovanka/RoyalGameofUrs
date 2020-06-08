from GreedyPlayer import GreedyPlayerClass
import random
import copy

class MinMaxPlayerClass(GreedyPlayerClass):

    rosette = [4,8,16]

    def getChance(self, n):
        diceChance = [1,4,6,4,1]
        return diceChance[n]

    def evalBoard(self, enemyPos, selfPos, prefSelfPos):
        # advDist = self.evaluate(enemyPos) - self.evaluate(selfPos)
        # for i in range(len(selfPos)):
        #     if not (prefSelfPos[i][0] in self.rosette) and selfPos[i][0] in self.rosette:
        #         advDist += 2
        advDist = (15-enemyPos) - (15-selfPos)
        if not prefSelfPos in self.rosette and selfPos in self.rosette:
            advDist += 2
        return advDist

    # pos1 yang dimakan ,pos2 yang makan
    def checkEat(self, pos1, pos2):
        newpos = pos2
        # for i in pos1:
        #     if i in pos2 and not(i in self.rosette) and i > 4 and i < 13:
        #         newpos.append(0)
        #     else:
        #         newpos.append(i)
        if pos1 == pos2 and not pos1 == 8 and pos1 > 4 and pos1 < 13:
            newpos = 0
        return newpos

    def simulateMovement(self, pos1,pos2):
        return

    def canmove(self, moveto, enemy):
        if moveto > 15:
            return False
        else:
            if moveto == enemy and moveto in [8]:
                return False
        return True 

    # player = -1 => enemy, player = 1 => self
    def testMinMax(self, n, enemyPos: int, selfPos: int, player=1, iteration=3):
        if player == 1:
            if n > -1:
                oldPionPosition = copy.copy(selfPos)
                currPionPosition = copy.copy(selfPos)
                currPionPosition += n
                if self.canmove(currPionPosition, enemyPos):
                    enemyPos = self.checkEat(enemyPos, currPionPosition)
                    if not (currPionPosition in self.rosette):
                        player *= -1
                    if iteration > 0:
                        x = self.testMinMax(-1, enemyPos, currPionPosition, player, iteration-1)
                        print(x)
                        return x
                    else:
                        x = self.evalBoard(enemyPos, currPionPosition, oldPionPosition)
                        print(x)
                        return x
                else:
                    if iteration > 0:
                        x = self.testMinMax(-1, enemyPos,oldPionPosition,-1,iteration-1)
                        print(x)
                        return x
                    else:
                        x = self.evalBoard(enemyPos, oldPionPosition, oldPionPosition)
                        print(x)
                        return x
            else:
                values = []
                for i in range(5):
                    oldPionPosition = copy.copy(selfPos)
                    currPionPosition = copy.copy(selfPos)
                    currPionPosition += i
                    if self.canmove(currPionPosition, enemyPos):
                        nextenemypos = self.checkEat(enemyPos, currPionPosition)
                        if not (currPionPosition in self.rosette):
                            player *= -1
                        if iteration > 0:
                            values.append(self.testMinMax(-1, nextenemypos, currPionPosition, player, iteration-1) * self.getChance(i))
                        else:
                            values.append(self.evalBoard(nextenemypos, currPionPosition, oldPionPosition) * self.getChance(i))
                    else:
                        if iteration > 0:
                            values.append(self.testMinMax(-1,enemyPos, oldPionPosition, -1, iteration-1) * self.getChance(i))
                        else:
                            values.append(self.evalBoard(enemyPos, oldPionPosition, oldPionPosition) * self.getChance(i))
                x = max(values)
                print(values, iteration)
                return x
        elif player == -1:
            values = []
            for i in range(5):
                oldEnemyPosition = copy.copy(enemyPos)
                currEnemyPosition = copy.copy(enemyPos)
                currEnemyPosition += i
                if self.canmove(currEnemyPosition, selfPos):
                    nextPlayerPos = self.checkEat(selfPos, currEnemyPosition)
                    if not (currEnemyPosition in self.rosette):
                        player *= -1
                    if iteration > 0:
                        values.append(self.testMinMax(-1, currEnemyPosition, nextPlayerPos, player, iteration-1) * self.getChance(i))
                    else:
                        values.append(self.evalBoard(currEnemyPosition, nextPlayerPos, selfPos) * self.getChance(i))
                else:
                    if iteration > 0 :
                        values.append(self.testMinMax(-1, oldEnemyPosition, selfPos, 1, iteration-1) * self.getChance(i))
                    else:
                        values.append(self.evalBoard(oldEnemyPosition, selfPos, selfPos))
            x = min(values)
            print(values, iteration)
            return x
        
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
