from Player import *
from Board import *
from GreedyPlayer import *
from MinMaxPlayer import *
from Utils import *

if __name__ == "__main__":
    minmaxwin = 0
    greedywin = 0
    for i in range(10):
        p1 = MinMaxPlayerClass("MinMax Bot", [1, "Bot"])
        p2 = GreedyPlayerClass("Greedy Bot", [2, "Bot"])
        board = BoardClass()

        randomNum = turnRandomizer2()
        p1, p2 = turnSetter(p1, p2, randomNum)
        # if randomNum == 1:
            # print(p1.name + " goes first.")
        # elif randomNum == 2:
            # print(p2.name + " goes first")

        while board.getGameFinished() == False:
            diceResult = diceRoll()
            if p1.getIsActive() == True:
                movedIndex = p1.minmax(diceResult, p2.getPionPositionNoId(), p1.getPionPositionNoId())
                isMoved, changeTurn, enemyDisplaced = p1.pionArray[movedIndex].move(diceResult, p2.getPionPosition(), p1.getPionPosition())

                if p1.checkWin() == True:
                    board.setGameFinished()
                    minmaxwin += 1
                    break

                if changeTurn == True:
                    p1, p2 = turnSetter(p1, p2, 2)
                    # print("Next round is " + p2.name + "'s turn!")
                # else:
                    # print("Next round is " + p1.name + "'s turn!")

                if enemyDisplaced > -1:
                    p2.pionKnockback(enemyDisplaced)


            elif p2.getIsActive() == True:
                movedIndex, best = p2.bestPion(diceResult, p1.getPionPosition())
                isMoved, changeTurn, enemyDisplaced = p2.pionArray[movedIndex].move(diceResult, p1.getPionPosition(), p2.getPionPosition())

                if p2.checkWin() == True:
                    board.setGameFinished()
                    greedywin += 1
                    break

                if changeTurn == True:
                    p1, p2 = turnSetter(p1, p2, 1)
                    # print("Next round is " + p1.name + "'s turn!")
                # else:
                    # print("Next round is " + p2.name + "'s turn!")

                if enemyDisplaced > -1:
                    p1.pionKnockback(enemyDisplaced)

    print("finished \n\n")
    print("minmax", minmaxwin)
    print("greedy", greedywin)
            # print(p1.getPionPosition())
            # print(p2.getPionPosition())
            # board.updateBoard(p1.getPionPosition(), p2.getPionPosition())
            # board.drawBoard()

    # p1 = PlayerClass("Player 1", [1, "Human"])
    # p2 = GreedyPlayerClass("Player 2", [2, "Bot"])
    # board = BoardClass()
    #
    # activePlayer = turnRandomizer(p1, p2)
    #
    # turnInfo(activePlayer)
    # board.drawBoard()
    #
    #
    # if activePlayer.identifier[1] == "Human":
    #     humanInfo(p1, p2)
    #     humanAction(activePlayer, p1, p2)
    #
    # board.updateBoard(p1.getPionPosition(), p2.getPionPosition())
    # board.drawBoard()

    # print(p1.pionArray[0].move(5, p2.positionArray, p1.positionArray))
    # print(p1.getPionPosition())
    # print(p2.getPionPosition())
    # board.updateBoard(p1.getPionPosition(), p2.getPionPosition())
    # board.drawBoard()
    # # print(p1.pionArray[0].nextRosette())
    # # print(p1.getPionPosition())
    # p2.pionArray[0].move(3,p1.getPionPosition(),p2.getPionPosition())
    # board.updateBoard(p1.getPionPosition(), p2.getPionPosition())
    # board.drawBoard()
    # board.updateBoard(p1.getPionPosition(), p2.getPionPosition())
    # board.drawBoard()