from random import randint 

name = 'Hack_of_Clans'

def moveTo(x , y , Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] < y) * 2 + 1
    if position[1] == y:
        return (position[0] > x) * 2 + 2
    if randint(1, 2) == 1:
        return (position[0] > x) * 2 + 2
    else:
        return (position[1] < y) * 2 + 1

def checkEnemy(x, y, Pirate):
    possible_moves = []
    if pirate.investigate_up()[1] == "enemy":
        possible_moves.append(str(x) + "," + str(y-1))
    if pirate.investigate_right()[1] == "enemy":
        possible_moves.append(str(x+1) + "," + str(y))
    if pirate.investigate_down()[1] == "enemy":
        possible_moves.append(str(x) + "," + str(y+1))
    if piate.investigate_left()[1] == "enemy":
        possible_moves.append(str(x-1) + "," + str(y))
    if pirate.investigate_ne()[1] == "enemy":
        possible_moves.append(str(x+1) + "," + str(y-1))
    if pirate.investigate_se()[1] == "enemy":
        possible_moves.append(str(x+1) + "," + str(y+1))
    if pirate.investigate_sw()[1] == "enemy":
        possible_moves.append(str(x-1) + "," + str(y+1))
    if pirate.investigate_nw()[1] == "enemy":
        possible_moves.append(str(x-1) + "," + str(y-1))

    if len(possible_moves) == 0:
        return None

    rand_index = randint(0,len(possible_moves)-1)
    return possible_moves[index]

def ActPirate(pirate):
    island_cord = getIslandCord(pirate)                         #Assumed saved in team signal
    x,y = pirate.getPosition()
    status = pirate.trackPlayers()
    for index in range(1,len(island_cord)):                     #For moving to a random position for attacking a enemy
        island_x,island_y = island_cord[index].split(",")
        if x == island_x and y == island_y and status[index-1] != "myCaptured":
            if checkEnemy(pirate(x,y,pirate)) != None:
                goto_x, goto_y = checkEnemy.split(",")
                return moveTo(int(x), int(y), pirate)

    for index in range(1,len(island_cord)):                     #For return of attacker to middle spot after attacking
        island_x,island_y = island_cord[index].split(",")
        if island_cord[index] != "" and abs(x - island_x) <= 1 and abs(y - island_y) <= 1:
            return moveTo(island_x, island_y)

def ActTeam(team):
    pass