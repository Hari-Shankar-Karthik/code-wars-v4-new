from utils import pirate_movements
from random import randint

name = "gradual_defense"

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

def updateIslandCord(pirate):
    up = pirate.investigate_up()[0]
    ne = pirate.investigate_ne()[0]
    nw = pirate.investigate_nw()[0]
    down = pirate.investigate_down()[0]
    se = pirate.investigate_se()[0]
    sw = pirate.investigate_sw()[0]
    right = pirate.investigate_right()[0]
    left = pirate.investigate_left()[0]
    x, y = pirate.getPosition()

    team_signal = pirate.getTeamSignal()

    if (up[:-1] == "island"):

        island_no = int(up[-1])

        if (up == ne and up == nw):
            island_x = x 
            island_y = y - 2
        elif (up == ne):
            island_x = x + 1
            island_y = y - 2
        else:
            island_x = x - 1
            island_y = y - 2
    
        if(team_signal[2*int(island_no)-2] == " "):
            team_signal = team_signal[0:2*int(island_no)-2] + chr(island_x + 63) + chr(island_y + 63) + team_signal[2*int(island_no):]

    elif (down[:-1] == "island"):

        island_no = down[-1]

        if (down == se and down == sw):
            island_x = x
            island_y = y + 2
        elif (down == se):
            island_x = x + 1
            island_y = y + 2
        else:
            island_x = x - 1
            island_y = y + 2

        if(team_signal[2*int(island_no)-2] == " "):
            team_signal = team_signal[0:2*int(island_no)-2] + chr(island_x + 63) + chr(island_y + 63) + team_signal[2*int(island_no):]

    elif (left[:-1] == "island"):

        island_no = left[-1]

        if (left == nw and left == sw):
            island_x = x - 2
            island_y = y
        elif (left == nw):
            island_x = x - 2
            island_y = y - 1
        else:
            island_x = x - 2
            island_y = y + 1

        if(team_signal[2*int(island_no)-2] == " "):
            team_signal = team_signal[0:2*int(island_no)-2] + chr(island_x + 63) + chr(island_y + 63) + team_signal[2*int(island_no):]

    elif (right[:-1] == "island"):

        island_no = right[-1]

        if(right == ne and right == se):
            island_x = x + 2
            island_y = y
        elif(right == ne):
            island_x = x + 2
            island_y = y - 1
        else:
            island_x = x + 2
            island_y = y + 1

        if(team_signal[2*int(island_no)-2] == " "):
            team_signal = team_signal[0:2*int(island_no)-2] + chr(island_x + 63) + chr(island_y + 63) + team_signal[2*int(island_no):]
    
    elif (ne[:-1] == "island"):

        island_no = ne[-1]

        island_x = x + 2
        island_y = y - 2

        if(team_signal[2*int(island_no)-2] == " "):
            team_signal = team_signal[0:2*int(island_no)-2] + chr(island_x + 63) + chr(island_y + 63) + team_signal[2*int(island_no):]

    elif (se[:-1] == "island"):

        island_no = se[-1]

        island_x = x + 2
        island_y = y + 2

        if(team_signal[2*int(island_no)-2] == " "):
            team_signal = team_signal[0:2*int(island_no)-2] + chr(island_x + 63) + chr(island_y + 63) + team_signal[2*int(island_no):]

        pirate.setTeamSignal(team_signal)

    elif (nw[:-1] == "island"):

        island_no = nw[-1]

        island_x = x - 2
        island_y = y - 2

        if(team_signal[2*int(island_no)-2] == " "):
            team_signal = team_signal[0:2*int(island_no)-2] + chr(island_x + 63) + chr(island_y + 63) + team_signal[2*int(island_no):]

    elif (sw[:-1] == "island"):

        island_no = sw[-1]

        island_x = x - 2
        island_y = y + 2

        if(team_signal[2*int(island_no)-2] == " "):
            team_signal = team_signal[0:2*int(island_no)-2] + chr(island_x + 63) + chr(island_y + 63) + team_signal[2*int(island_no):]


def groupDefender(pirate):
    state = pirate.trackPlayers()
    team_signal = pirate.getTeamSignal()
    for index in range(3,len(state)):
        start_index = index*10              # The number 10 can be changed
        island_no = index-2
        if state[index] == "oppCapturing" and team_signal[2*island_no-2] != " " and team_signal[2*island_no-1] != " "and randint(1,10) == 1:    #Probability can be changed
            island_x = team_signal[2*island_no-2]
            island_y = team_signal[2*island_no-1]
            team_signal = team_signal[0:start_index] + chr(int(pirate.getID())+63) + team_signal[start_index+1:]
            pirate.setTeamSignal(team_signal)
            # pirate.moveTo(x,y,pirate)

def ActPirate(pirate):
    pirate_signal  = pirate.getSignal()
    if pirate_signal == "":
        pirate_signal = " "*100
    pirate.setSignal(pirate_signal)
    updateIslandCord(pirate)
    groupDefender(pirate)
    x, y = pirate.getPosition()
    team_signal = pirate.getTeamSignal()
    status = pirate.trackPlayers()
    for island_no in range(1,4):
        for index in range(0,10):
            if(team_signal[island_no*10+index] == chr(int(pirate.getID()))):
                island_x = ord(team_signal[2*island_no-2]) - 63
                island_y = ord(team_signal[2*island_no-1]) - 63
                pirate_signal = pirate.getSignal()
                pirate_signal = pirate_signal[:2] + chr(max(island_x-6,1)+63) + chr(max(island_y-6,1)+63) + pirate_signal[4:]
                pirate_signal = chr(x + 63) + chr(y + 63) + pirate_signal[2:]
                return moveTo(ord(pirate_signal[2])-63, ord(pirate_signal[3])-63, pirate)

    for island_no in range(1,4):
        for index in range(0,10):
            if(team_signal[island_no*10+index] == chr(int(pirate.getID()) + 63) and x == pirate_signal[2] and y == pirate_signal[3]):
                island_x = ord(team_signal[2*island_no-2]) - 63
                island_y = ord(team_signal[2*island_no-1]) - 63
                pirate_signal = pirate.getSignal()
                pirate_signal = pirate_signal[:2] + chr(island_x + 63) + chr(island_y + 63) + pirate_signal[4:]
                pirate_signal = chr(x + 63) + chr(y + 63) + pirate_signal[2:]
                return moveTo(ord(pirate_signal[2])-63, ord(pirate_signal[3])-63, pirate)

    for island_no in range(1,4):
        island_x = team_signal[2*island_no-2]
        island_y = team_signal[2*island_no-1]
        if island_x != " " and island_y != " " and status[island_no-1] != "myCaptured":
            rand = randint(1,10)
            if rand <= 2:
                return moveTo(ord(island_x)-63, ord(island_y)-63, pirate)

    return randint(1,4) 
        
def ActTeam(team):
    team_signal = team.getTeamSignal()
    if team_signal == "":
        team_signal = " "*100
        team.setTeamSignal(team_signal)

    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)
