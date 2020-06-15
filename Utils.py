import random

def turnRandomizer(p1, p2):
    randomNum = random.randint(1,2)
    if randomNum == 1:
        print("Player 1 goes first")
        return p1
    elif randomNum == 2:
        print("Player 2 goes first")
        return p2

def turnRandomizer2():
    return random.randint(1, 2)

def turnSetter(p1, p2, turn):
    if turn == 1:
        p1.setIsActive(True)
        p2.setIsActive(False)
    elif turn == 2:
        p1.setIsActive(False)
        p2.setIsActive(True)

    return p1, p2

def diceRoll():
    randomNum1 = random.randint(0, 1)
    randomNum2 = random.randint(0, 1)
    randomNum3 = random.randint(0, 1)
    randomNum4 = random.randint(0, 1)
    total = randomNum1 + randomNum2 + randomNum3 + randomNum4
    print("Dice roll result: " + str(total))
    return total

def humanInfo(p1, p2):
    p1Pions = []
    p2Pions = []

    for i in p1.getPionPosition():
        if i[0] == 0:
            p1Pions.append(i[1])

    for j in p2.getPionPosition():
        if i[0] == 0:
            p2Pions.append(j[1])

    print("\nPlayer 1's Pions:")
    print(p1Pions)
    print("\nPlayer 2's Pions:")
    print(p2Pions)

def humanAction(activePlayer, p1, p2):
    inactivePlayer = None
    if activePlayer.identifier[0] == 1:
        inactivePlayer = p2
    else:
        inactivePlayer = p1

    option = int(input("\nWhat would you like to do?\n [1]. Roll dice\n [2]. Table flip (concede)\n"))
    move = int

    if option == 1:
        move = diceRoll()

    elif option == 2:
        print("You flipped the table and conceded the game.")

    if move == 0:
        print("You rolled a 0 and ended your turn.")
        return

    playerPions = []
    for i in activePlayer.getPionPosition():
        playerPions.append(i[1])

    print("\nWhich piece would you like to move?")
    print(playerPions)
    option = input()

    if activePlayer.identifier[0] == 1:
        moveHumanPion(p1, move, option, p2)
    else:
        moveHumanPion(p2, move, option, p1)

def moveHumanPion(player, move, option, opponent):
    choice = option
    i = int
    if player.identifier == 2:
        choice = choice.upper()
    else:
        choice = int(choice) - 1
        choice = str(choice)

    for j in range(len(player.pionArray)):
        if player.pionArray[j].identifier == option:
            i = j
            break

    player.pionArray[i].move(move, opponent.getPionPosition(), player.getPionPosition())



def turnInfo(activePlayer):
    print(activePlayer.name + "'s turn!")
