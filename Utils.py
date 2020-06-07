import random

def turnRandomizer(p1, p2):
    randomNum = random.randint(1,1)
    if randomNum == 1:
        print("Player 1 goes first")
        return p1
    elif randomNum == 2:
        print("Player 2 goes first")
        return p2

def diceRoll():
    randomNum1 = random.randint(0, 1)
    randomNum2 = random.randint(0, 1)
    randomNum3 = random.randint(0, 1)
    randomNum4 = random.randint(0, 1)
    total = randomNum1 + randomNum2 + randomNum3 + randomNum4
    print("Dice roll result: " + str(total))
    return total

def humanInfo(board, p1, p2):
    p1Pions = []
    p2Pions = []

    for i in p1.getPionPosition():
        p1Pions.append(i[1])

    for j in p2.getPionPosition():
        p2Pions.append(j[1])

    print("\nPlayer 1's Pions:")
    print(p1Pions)
    print("\nPlayer 2's Pions:")
    print(p2Pions)

def humanAction():
    option = int(input("\nWhat would you like to do?\n [1]. Roll dice\n [2]. Table flip (concede)\n"))

    if option == 1:
        diceRoll()

    elif option == 2:
        print("You flipped the table and conceded the game.")

def turnInfo(activePlayer):
    print(activePlayer.name + "'s turn!")

