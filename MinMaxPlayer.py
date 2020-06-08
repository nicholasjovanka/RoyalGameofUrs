from GreedyPlayer import GreedyPlayerClass
import random

class MinMaxPlayerClass(GreedyPlayerClass):

    rosette = [4,8,16]

    def getChance(self, n):
        diceChance = [0.0625,0.25,0.375,0.25,0.0625]
        return diceChance[n]

    def evalBoard(self, enemyPos, selfPos, prefSelfPos):
        # advDist = self.evaluate(enemyPos) - self.evaluate(selfPos)
        # for i in range(len(selfPos)):
        #     if not (prefSelfPos[i][0] in self.rosette) and selfPos[i][0] in self.rosette:
        #         advDist += 2
        advDist = enemyPos - selfPos
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
                oldPionPosition, currPionPosition = selfPos.copy()
                currPionPosition += n
                if self.canmove(currPionPosition, enemyPos):
                    enemyPos = self.checkEat(enemyPos, currPionPosition)
                    if not currPionPosition in self.rosette:
                        player *= -1
                    if iteration > 0:
                        return self.testMinMax(-1, enemyPos, currPionPosition, player, iteration-1)
                    else:
                        return self.evalBoard(enemyPos, currPionPosition, oldPionPosition)
                else:
                    if iteration > 0:
                        return self.testMinMax(-1, enemyPos,oldPionPosition,-1,iteration-1)
                    else:
                        return self.evalBoard(enemyPos, oldPionPosition, oldPionPosition)
            else:
                values = []
                for i in range(5):
                    oldPionPosition, currPionPosition = selfPos.copy()
                    currPionPosition += i
                    if self.canmove(currPionPosition, enemyPos):
                        nextenemypos = self.checkEat(enemyPos, currPionPosition)
                        if not currPionPosition in self.rosette:
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
                return values.index(max(values))
        elif player == -1:
            values = []
            for i in range(5):
                oldEnemyPosition, currEnemyPosition = enemyPos.copy()
                currEnemyPosition += i
                if self.canmove(currEnemyPosition, selfPos):
                    nextPlayerPos = self.checkEat(selfPos, currEnemyPosition)
                    if not currEnemyPosition in self.rosette:
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
                return values.index(min(values))
        
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
