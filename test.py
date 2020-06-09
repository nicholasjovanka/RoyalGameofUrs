from MinMaxPlayer import MinMaxPlayerClass

if __name__ == "__main__":
    x = MinMaxPlayerClass(1,'bot')
    p1 = [0,0,7,0,0,0,0]
    p2 = [0,0,9,0,0,0,0]
    x.minmax(2,p2,p1)

