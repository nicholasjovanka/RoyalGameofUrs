class PionClass:
    identifier : str
    position : int
    safe : bool
    finish : bool
    minpos = 0
    maxpos = 15
    rosette = [4,8,14]

    def __init__(self, identifier, initialPosition= 0):
        self.position = initialPosition
        self.safe = True
        self.finish = False
        self.identifier = identifier
        
    def canmove(self,n,enemyPos, playerPos):
        temp = self.position + n
        # if the pion will land more than the goal, decline
        if(temp > self.maxpos):
            return False
        else:
            # if the player lands on rosette in the middle while an enemy is there
            if temp in [8] and (temp in enemyPos or temp in playerPos):
                return False
            # if the pion will land on teammate, decline
            elif temp in playerPos and temp != 15:
                return False
            # player can move normally
            return True

    def move(self,n, opponentPos, selfPos):
        enemyPos = []
        playerPos = []

        for i in opponentPos:
            enemyPos.append(i[0])

        for j in selfPos:
            playerPos.append(j[0])

        canMove = self.canmove(n, enemyPos, playerPos)
        # (canmove,indicate next turn, enemy eaten)
        if(canMove == False):
            return (False,True,-1)
        elif(self.position + n) in self.rosette:
            self.changeSafe(True)
            self.position += n
            return (True,False,-1)
        else:
            self.changeSafe(False)
            self.position += n
            if self.position in enemyPos and self.position in [5, 6, 7, 8, 9, 10, 11, 12]:
                return(True,True,self.position)
            return (True,True,-1)

    def changeSafe(self, state):
        self.safe = state

    def nextRosette(self):
        distance = 99
        rosette = 0
        if self.position == 15:
            return(0,0)
        for i in range(3):
            nextrs = self.rosette[i]
            temp = nextrs - self.position
            if temp < distance and temp >= 0:
                rosette, distance = i, temp
        return(rosette,distance)

    def distanceToGoal(self):
        return self.maxpos - self.position
    
