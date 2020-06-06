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
            if i == 1:
                self.boardState[0,3] = '[X]'

            elif i == 2:
                self.boardState[0,2] = '[X]'

            elif i == 3:
                self.boardState[0,1] = '[X]'

            elif i == 4:
                self.boardState[0,0] = '(X)'

            elif i == 5:
                self.boardState[1,0] = '[X]'

            elif i == 6:
                self.boardState[1,1] = '[X]'

            elif i == 7:
                self.boardState[1,2] = '[X]'

            elif i == 8:
                self.boardState[1,3] = '(X)'

            elif i == 9:
                self.boardState[1,4] = '[X]'

            elif i == 10:
                self.boardState[1,5] = '[X]'

            elif i == 11:
                self.boardState[1,6] = '[X]'

            elif i == 12:
                self.boardState[1,7] = '[X]'

            elif i == 13:
                self.boardState[0,7] = '[X]'

            elif i == 14:
                self.boardState[0,6] = '[X]'

        for j in p2PionsPosition:
            if j == 1:
                self.boardState[2, 3] = '[O]'

            if j == 2:
                self.boardState[2, 2] = '[O]'

            if j == 3:
                self.boardState[2, 1] = '[O]'

            if j == 4:
                self.boardState[2, 0] = '(O)'

            if j == 5:
                self.boardState[1, 0] = '[O]'

            if j == 6:
                self.boardState[1, 1] = '[O]'

            if j == 7:
                self.boardState[1, 2] = '[O]'

            if j == 8:
                self.boardState[1, 3] = '(O)'

            if j == 9:
                self.boardState[1, 4] = '[O]'

            if j == 10:
                self.boardState[1, 5] = '[O]'

            if j == 11:
                self.boardState[1, 6] = '[O]'

            if j == 12:
                self.boardState[1, 7] = '[O]'

            if j == 13:
                self.boardState[2, 7] = '[O]'

            if j == 14:
                self.boardState[2, 6] = '[O]'

    def drawBoard(self):
        print(self.boardState)