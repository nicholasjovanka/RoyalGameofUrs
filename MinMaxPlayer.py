from GreedyPlayer import GreedyPlayerClass
import random
import copy

class MinMaxPlayerClass(GreedyPlayerClass):

    rosette = [4,8,14]

    def getChance(self, n):
        diceChance = [1,4,6,4,1]
        return diceChance[n]

    def evalBoard(self, enemyPos, selfPos, prefSelfPos):
        advDist = self.evaluate(enemyPos) - self.evaluate(selfPos)
        for i in range(len(selfPos)):
            if not (prefSelfPos[i] in self.rosette) and selfPos[i] in self.rosette:
                advDist += 2
            if selfPos[i] == 15:
                # print("finish")
                advDist += 10000
        # advDist = (15-enemyPos) - (15-selfPos)
        # if not prefSelfPos in self.rosette and selfPos in self.rosette:
        #     advDist += 2
        return advDist

    # pos1 yang dimakan ,pos2 yang makan
    def checkEat(self, pos1, pos2):
        newpos = []
        for i in pos1:
            if i in pos2 and not(i in self.rosette) and i > 4 and i < 13:
                newpos.append(0)
            else:
                newpos.append(i)
        # if pos1 == pos2 and not pos1 == 8 and pos1 > 4 and pos1 < 13:
        #     newpos = 0
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

    def canmoveArray(self, moveto, selfPos, enemyPos):
        if moveto > 15:
            return False
        else:
            if moveto == 8 and (moveto in enemyPos or moveto in selfPos):
                return False
            # if the pion will land on teammate, decline
            elif moveto in selfPos:
                return False
        return True

    # player = -1 => enemy, player = 1 => self
    # def testMinMax(self, n, enemyPos: int, selfPos: int, player=1, iteration=3):
    #     if player == 1:
    #         if n > -1:
    #             oldPionPosition = copy.copy(selfPos)
    #             currPionPosition = copy.copy(selfPos)
    #             currPionPosition += n
    #             if self.canmove(currPionPosition, enemyPos):
    #                 enemyPos = self.checkEat(enemyPos, currPionPosition)
    #                 if not (currPionPosition in self.rosette):
    #                     player *= -1
    #                 if iteration > 0:
    #                     x = self.testMinMax(-1, enemyPos, currPionPosition, player, iteration-1)
    #                     print(x)
    #                     return x
    #                 else:
    #                     x = self.evalBoard(enemyPos, currPionPosition, oldPionPosition)
    #                     print(x)
    #                     return x
    #             else:
    #                 if iteration > 0:
    #                     x = self.testMinMax(-1, enemyPos,oldPionPosition,-1,iteration-1)
    #                     print(x)
    #                     return x
    #                 else:
    #                     x = self.evalBoard(enemyPos, oldPionPosition, oldPionPosition)
    #                     print(x)
    #                     return x
    #         else:
    #             values = []
    #             for i in range(5):
    #                 oldPionPosition = copy.copy(selfPos)
    #                 currPionPosition = copy.copy(selfPos)
    #                 currPionPosition += i
    #                 if self.canmove(currPionPosition, enemyPos):
    #                     nextenemypos = self.checkEat(enemyPos, currPionPosition)
    #                     if not (currPionPosition in self.rosette):
    #                         player *= -1
    #                     if iteration > 0:
    #                         values.append(self.testMinMax(-1, nextenemypos, currPionPosition, player, iteration-1) * self.getChance(i))
    #                     else:
    #                         values.append(self.evalBoard(nextenemypos, currPionPosition, oldPionPosition) * self.getChance(i))
    #                 else:
    #                     if iteration > 0:
    #                         values.append(self.testMinMax(-1,enemyPos, oldPionPosition, -1, iteration-1) * self.getChance(i))
    #                     else:
    #                         values.append(self.evalBoard(enemyPos, oldPionPosition, oldPionPosition) * self.getChance(i))
    #             x = max(values)
    #             print(values, iteration)
    #             return x
    #     elif player == -1:
    #         values = []
    #         for i in range(5):
    #             oldEnemyPosition = copy.copy(enemyPos)
    #             currEnemyPosition = copy.copy(enemyPos)
    #             currEnemyPosition += i
    #             if self.canmove(currEnemyPosition, selfPos):
    #                 nextPlayerPos = self.checkEat(selfPos, currEnemyPosition)
    #                 if not (currEnemyPosition in self.rosette):
    #                     player *= -1
    #                 if iteration > 0:
    #                     values.append(self.testMinMax(-1, currEnemyPosition, nextPlayerPos, player, iteration-1) * self.getChance(i))
    #                 else:
    #                     values.append(self.evalBoard(currEnemyPosition, nextPlayerPos, selfPos) * self.getChance(i))
    #             else:
    #                 if iteration > 0 :
    #                     values.append(self.testMinMax(-1, oldEnemyPosition, selfPos, 1, iteration-1) * self.getChance(i))
    #                 else:
    #                     values.append(self.evalBoard(oldEnemyPosition, selfPos, selfPos))
    #         x = min(values)
    #         print(values, iteration)
    #         return x
        
    # player = -1 => enemy, player = 1 => self
    def minmax(self, n, enemyPos, selfPos, player=1, iteration=3):
        if player == 1:
            if n > -1:
                values = []
                for i in range(len(selfPos)):
                    oldPionPosition = selfPos.copy()
                    currPionPosition = selfPos.copy()
                    oldEnemyPosition = enemyPos.copy()
                    currPionPosition[i] += n
                    nxtplayer = 1
                    if self.canmoveArray(currPionPosition[i], oldPionPosition, enemyPos):
                        newEnemyPos = self.checkEat(oldEnemyPosition, currPionPosition)
                        if not (currPionPosition[i] in self.rosette):
                            nxtplayer = -1
                        if iteration > 0:
                            x = self.minmax(-1, newEnemyPos, currPionPosition, nxtplayer, iteration-1)
                            values.append(x)
                        else:
                            print(currPionPosition, newEnemyPos, nxtplayer)
                            x = self.evalBoard(newEnemyPos, currPionPosition, oldPionPosition)
                            values.append(x)
                    else:
                        # if iteration > 0:
                        #     x = self.minmax(-1, oldEnemyPosition, oldPionPosition,-1,iteration-1)
                        #     values.append(x)
                        # else:
                        #     print(oldPionPosition, oldEnemyPosition, nxtplayer)
                        #     x = self.evalBoard(oldEnemyPosition, oldPionPosition, oldPionPosition)
                        #     values.append(x)
                        values.append(-999999)
                print(values)
                return values.index(max(values))
            else:
                values = []
                for j in range(len(selfPos)):
                    rollResult = []
                    for i in range(5):
                        oldPionPosition =  selfPos.copy()
                        currPionPosition = selfPos.copy()
                        oldEnemyPosition = enemyPos.copy()
                        currPionPosition[j] += i
                        nxtplayer = 1
                        if self.canmoveArray(currPionPosition[j], oldPionPosition, enemyPos):
                            nextenemypos = self.checkEat(oldEnemyPosition, currPionPosition)
                            if not (currPionPosition[j] in self.rosette):
                                nxtplayer = -1
                            if iteration > 0:
                                rollResult.append(self.minmax(-1, nextenemypos, currPionPosition, nxtplayer, iteration-1) * self.getChance(i))
                            else:
                                # print(currPionPosition, nextenemypos, nxtplayer)
                                rollResult.append(self.evalBoard(nextenemypos, currPionPosition, oldPionPosition) * self.getChance(i))
                        else:
                            # if iteration > 0:
                            #     rollResult.append(self.minmax(-1,oldEnemyPosition, oldPionPosition, -1, iteration-1) * self.getChance(i))
                            # else:
                            #     # print(oldPionPosition, enemyPos, nxtplayer)
                            #     rollResult.append(self.evalBoard(oldEnemyPosition, oldPionPosition, oldPionPosition) * self.getChance(i))
                            rollResult.append(-99999)
                    values.append(max(rollResult))
                x = max(values)
                # print(values)
                return x
        elif player == -1:
            values = []
            for j in range(len(enemyPos)):
                rollResult = []
                for i in range(5):
                    oldEnemyPosition = copy.copy(enemyPos)
                    currEnemyPosition = copy.copy(enemyPos)
                    oldPlayerPos = selfPos.copy()
                    currEnemyPosition[j] += i
                    nxtplayer = -1
                    if self.canmoveArray(currEnemyPosition[j], enemyPos, selfPos):
                        nextPlayerPos = self.checkEat(oldPlayerPos, currEnemyPosition)
                        if not (currEnemyPosition[j] in self.rosette):
                            nxtplayer = 1
                        if iteration > 0:
                            rollResult.append(self.minmax(-1, currEnemyPosition, nextPlayerPos, nxtplayer, iteration-1) * self.getChance(i))
                        else:
                            # print(nextPlayerPos, currEnemyPosition, player)
                            rollResult.append(self.evalBoard(currEnemyPosition, nextPlayerPos, selfPos) * self.getChance(i))
                    else:
                        if iteration > 0 :
                            rollResult.append(self.minmax(-1, oldEnemyPosition, oldPlayerPos, 1, iteration-1) * self.getChance(i))
                        else:
                            # print(selfPos, oldEnemyPosition, player)
                            rollResult.append(self.evalBoard(oldEnemyPosition, oldPlayerPos, selfPos) * self.getChance(i))
                        # rollResult.append(99999)
                values.append(min(rollResult))
            x = min(values)
            print(values, iteration)
            return x