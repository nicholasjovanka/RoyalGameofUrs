import random

def turnRandomizer(p1, p2):
    randomNum = random.randint(1,2)
    if randomNum == 1:
        print("Player 1's Turn")
        return p1
    elif randomNum == 2:
        print("Player 2's Turn")
        return p2


