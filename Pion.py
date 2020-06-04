class Pion:
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
            return -1
        else:
            # if the pion will land on teammate, decline
            if temp in playerPos and temp != 8:
                return -1
            # if the player lands on rosette in the middle while an enemy is there
            elif (temp in enemyPos or temp in playerPos) and temp in self.rosette:
                return 0
            # player can move normally
            return 1

    def move(self,n, enemyPos, playerPos):
        status = self.canmove(n, enemyPos, playerPos)
        # indicate next turn
        if(status == -1):
            return 0
        elif(status == 0):
            self.position += 1+n
            return 1
        elif(self.position + n) in self.rosette:
            self.position += n
            return 2
        else:
            self.position += n
            return 3

    def changeSafe(self, state):
        self.safe = state
