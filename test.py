from MinMaxPlayer import MinMaxPlayerClass
from GreedyPlayer import GreedyPlayerClass

if __name__ == "__main__":
    # x = MinMaxPlayerClass(1,'bot')
    # print(x.canmoveArray(2,[0,0,7,0,0,0,0],[0,0,9,0,0,0,0]))
    # p1 = [0,0,7,0,0,0,0]
    # p2 = [0,0,9,0,0,0,0]
    # print(x.minmax(2,p2,p1))
    # print(p1.index(max(p1)))
    # print(max([-2016, 2592, -576, 3240, -720, 3240, -720]))

    x = GreedyPlayerClass("Nicho", [1, "Bot"])
    y = GreedyPlayerClass("afew", [2,"bot"])
    x.pionArray[2].move(7, y.getPionPosition(), x.getPionPosition())
    y.pionArray[2].move(9, x.getPionPosition(), y.getPionPosition())
    print(y.getPionPosition())
    print(x.bestPion(2, y.getPionPosition()))
