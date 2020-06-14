from MinMaxPlayer import MinMaxPlayerClass
from GreedyPlayer import GreedyPlayerClass
import Utils

if __name__ == "__main__":
    x = MinMaxPlayerClass("Player 1",[1,'bot'], [15,15,15,15,15,15,15])
    # print(x.canmoveArray(2,[0,0,7,0,0,0,0],[0,0,9,0,0,0,0]))

    # p1 = [14,15,13,8,11,4,0]
    # p2 = [15,15,14,15,15,15,12]
    # print(x.minmax(1,p2,p1))

    # print(x.evalBoard(p2, [14,7,0,0,0,6,0], p1))
    # Utils.diceRoll()
    # Utils.diceRoll()

    x.checkWin();