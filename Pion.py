class PionClass:
    position : int
    safe : bool
    finish : bool
    minpos = 0
    maxpos = 15
    rosette = [4,8,14]

    def __init__(self):
        self.position = 0
        self.safe = True
        self.finish = False
        
    def canmove(self,n,enemyPos, playerPos):
        temp = self.position + n
        # if the pion will land more than the goal, decline
        if(temp > self.maxpos):
            return False
        else:
            # if the player lands on rosette in the middle while an enemy is there
            if temp in self.rosette and (temp in enemyPos or temp in playerPos):
                return False
            # if the pion will land on teammate, decline
            elif temp in playerPos:
                return False
            # player can move normally
            return True

    def move(self,n, enemyPos, playerPos):
        canMove = self.canmove(n, enemyPos, playerPos)
        # (canmove,indicate next turn, enemy eaten)
        if(canMove == False):
            return (False,False,-1)
        elif(self.position + n) in self.rosette:
            self.changeSafe(True)
            self.position += n
            return (True,False,-1)
        else:
            self.changeSafe(False)
            self.position += n
            if self.position in enemyPos:
                return(True,True,enemyPos)
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
    
