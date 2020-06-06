import numpy as np
import Player

class BoardClass:
    boardState = np.empty

    def __init__(self):
        self.boardState = np.array([['( )','[ ]','[ ]','[ ]','---','---','( )','[ ]',],
                                    ['[ ]','[ ]','[ ]','( )','[ ]','[ ]','[ ]','[ ]',],
                                    ['( )','[ ]','[ ]','[ ]','---','---','( )','[ ]',]])

    def updateBoard(self, p1PionsPosition, p2PionsPosition):
        for i in p1PionsPosition:
            if i == 1:
                self.boardState[0,3] = '[X]'

            if i == 2:
                self.boardState[0,2] = '[X]'

            if i == 3:
                self.boardState[0,1] = '[X]'

            if i == 4:
                self.boardState[0,0] = '(X)'

            if i == 5:
                self.boardState[1,0] = '[X]'

            if i == 6:
                self.boardState[1,1] = '[X]'

            if i == 7:
                self.boardState[1,2] = '[X]'

            if i == 8:
                self.boardState[1,3] = '(X)'

            if i == 9:
                self.boardState[1,4] = '[X]'

            if i == 10:
                self.boardState[1,5] = '[X]'

            if i == 11:
                self.boardState[1,6] = '[X]'

            if i == 12:
                self.boardState[1,7] = '[X]'

            if i == 13:
                self.boardState[0,7] = '[X]'

            if i == 14:
                self.boardState[0,6] = '[X]'

        for i in p2PionsPosition:
            if i == 1:
                self.boardState[2, 3] = '[X]'

            if i == 2:
                self.boardState[2, 2] = '[X]'

            if i == 3:
                self.boardState[2, 1] = '[X]'

            if i == 4:
                self.boardState[2, 0] = '(X)'

            if i == 5:
                self.boardState[1, 0] = '[X]'

            if i == 6:
                self.boardState[1, 1] = '[X]'

            if i == 7:
                self.boardState[1, 2] = '[X]'

            if i == 8:
                self.boardState[1, 3] = '(X)'

            if i == 9:
                self.boardState[1, 4] = '[X]'

            if i == 10:
                self.boardState[1, 5] = '[X]'

            if i == 11:
                self.boardState[1, 6] = '[X]'

            if i == 12:
                self.boardState[1, 7] = '[X]'

            if i == 13:
                self.boardState[2, 7] = '[X]'

            if i == 14:
                self.boardState[2, 6] = '[X]'

    def drawBoard(self):
        print(self.boardState)