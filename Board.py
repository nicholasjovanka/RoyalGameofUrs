import numpy as np
import Player

class BoardClass:
    boardState = np.empty

    def __init__(self):
        self.boardState = np.array([['( )','[ ]','[ ]','[ ]','---','---','( )','[ ]',],
                                    ['[ ]','[ ]','[ ]','( )','[ ]','[ ]','[ ]','[ ]',],
                                    ['( )','[ ]','[ ]','[ ]','---','---','( )','[ ]',]])

    def updateBoard(self, p1PionsPosition, p2PionsPosition):
        print(p1PionsPosition)
        print(p2PionsPosition)
        for i in p1PionsPosition:
            if i[0] == 1:
                self.boardState[0,3] = i[1]

            elif i[0] == 2:
                self.boardState[0,2] = i[1]

            elif i[0] == 3:
                self.boardState[0,1] = i[1]

            elif i[0] == 4:
                self.boardState[0,0] = i[1]

            elif i[0] == 5:
                self.boardState[1,0] = i[1]

            elif i[0] == 6:
                self.boardState[1,1] = i[1]

            elif i[0] == 7:
                self.boardState[1,2] = i[1]

            elif i[0] == 8:
                self.boardState[1,3] = i[1]

            elif i[0] == 9:
                self.boardState[1,4] = i[1]

            elif i[0] == 10:
                self.boardState[1,5] = i[1]

            elif i[0] == 11:
                self.boardState[1,6] = i[1]

            elif i[0] == 12:
                self.boardState[1,7] = i[1]

            elif i[0] == 13:
                self.boardState[0,7] = i[1]

            elif i[0] == 14:
                self.boardState[0,6] = i[1]

        for j in p2PionsPosition:
            if j[0] == 1:
                self.boardState[2, 3] = j[1]

            if j[0] == 2:
                self.boardState[2, 2] = j[1]

            if j[0] == 3:
                self.boardState[2, 1] = j[1]

            if j[0] == 4:
                self.boardState[2, 0] = j[1]

            if j[0] == 5:
                self.boardState[1, 0] = j[1]

            if j[0] == 6:
                self.boardState[1, 1] = j[1]

            if j[0] == 7:
                self.boardState[1, 2] = j[1]

            if j[0] == 8:
                self.boardState[1, 3] = j[1]

            if j[0] == 9:
                self.boardState[1, 4] = j[1]

            if j[0] == 10:
                self.boardState[1, 5] = j[1]

            if j[0] == 11:
                self.boardState[1, 6] = j[1]

            if j[0] == 12:
                self.boardState[1, 7] = j[1]

            if j[0] == 13:
                self.boardState[2, 7] = j[1]

            if j[0] == 14:
                self.boardState[2, 6] = j[1]

    def drawBoard(self):
        print("\nCurrent Board State: ")
        print(self.boardState)