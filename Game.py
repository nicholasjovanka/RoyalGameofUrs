from Player import *
from Board import *
from GreedyPlayer import *

if __name__ == "__main__":
    p1 = PlayerClass()
    p2 = GreedyPlayerClass()
    board = BoardClass()

    board.drawBoard()
    print(p1.pionArray[0].move(5, p2.positionArray, p1.positionArray))
    print(p1.getPionPosition())
    print(p2.getPionPosition())
    board.updateBoard(p1.getPionPosition(), p2.getPionPosition())
    board.drawBoard()
    # print(p1.pionArray[0].nextRosette())
    # print(p1.getPionPosition())
    p2.pionArray[0].move(3,p1.getPionPosition(),p2.getPionPosition())
    board.updateBoard(p1.getPionPosition(), p2.getPionPosition())
    board.drawBoard()
    board.updateBoard(p1.getPionPosition(), p2.getPionPosition())
    board.drawBoard()