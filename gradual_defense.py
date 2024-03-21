from random import randint

name = "gradual_defense"

def cipher(l):
    s = ""
    if type(l) is list:
        for item in l:
            if item != " ":
                s += chr(int(item) + 63)
            else:
                s += " "
        return s
    else:
        if l != " ":
            return chr(int(l) + 63)
        else:
            return " "

def decipher(s):
    if len(s) > 1:
        l = []
        for ch in s:
            if ch == " ":
                l.append(" ")
            else:
                l.append(ord(ch) - 63)
        return l
    else:
        if s != " ":
            return ord(s) - 63
        else:
            return " "

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
    
        if(team_signal[2*island_no-2] == " "):
            team_signal = team_signal[0:2*island_no-2] + cipher(island_x) + cipher(island_y) + team_signal[2*island_no:]

    elif (down[:-1] == "island"):

        island_no = int(down[-1])

        if (down == se and down == sw):
            island_x = x
            island_y = y + 2
        elif (down == se):
            island_x = x + 1
            island_y = y + 2
        else:
            island_x = x - 1
            island_y = y + 2

        if(team_signal[2*island_no-2] == " "):
            team_signal = team_signal[0:2*island_no-2] + cipher(island_x) + cipher(island_y) + team_signal[2*island_no:]

    elif (left[:-1] == "island"):

        island_no = int(left[-1])

        if (left == nw and left == sw):
            island_x = x - 2
            island_y = y
        elif (left == nw):
            island_x = x - 2
            island_y = y - 1
        else:
            island_x = x - 2
            island_y = y + 1

        if(team_signal[2*island_no-2] == " "):
            team_signal = team_signal[0:2*island_no-2] + cipher(island_x) + cipher(island_y) + team_signal[2*island_no:]

    elif (right[:-1] == "island"):

        island_no = int(right[-1])

        if(right == ne and right == se):
            island_x = x + 2
            island_y = y
        elif(right == ne):
            island_x = x + 2
            island_y = y - 1
        else:
            island_x = x + 2
            island_y = y + 1

        if(team_signal[2*island_no-2] == " "):
            team_signal = team_signal[0:2*island_no-2] + cipher(island_x) + cipher(island_y) + team_signal[2*island_no:]
    
    elif (ne[:-1] == "island"):

        island_no = int(ne[-1])

        island_x = x + 2
        island_y = y - 2

        if(team_signal[2*island_no-2] == " "):
            team_signal = team_signal[0:2*island_no-2] + cipher(island_x) + cipher(island_y) + team_signal[2*island_no:]

    elif (se[:-1] == "island"):

        island_no = int(se[-1])

        island_x = x + 2
        island_y = y + 2

        if(team_signal[2*island_no-2] == " "):
            team_signal = team_signal[0:2*island_no-2] + cipher(island_x) + cipher(island_y) + team_signal[2*island_no:]


    elif (nw[:-1] == "island"):

        island_no = int(nw[-1])

        island_x = x - 2
        island_y = y - 2

        if(team_signal[2*island_no-2] == " "):
            team_signal = team_signal[0:2*island_no-2] + cipher(island_x) + cipher(island_y) + team_signal[2*island_no:]

    elif (sw[:-1] == "island"):

        island_no = int(sw[-1])

        island_x = x - 2
        island_y = y + 2

        if(team_signal[2*island_no-2] == " "):
            team_signal = team_signal[0:2*island_no-2] + cipher(island_x) + cipher(island_y) + team_signal[2*island_no:]

    pirate.setTeamSignal(team_signal)

# def groupDefender(pirate):
#     state = pirate.trackPlayers()
#     team_signal = pirate.getTeamSignal()
#     for index in range(3,len(state)):
#         start_index = index*10              # The number 10 can be changed
#         island_no = index-2
#         if state[index] == "oppCapturing" and team_signal[2*island_no-2] != " " and team_signal[2*island_no-1] != " "and randint(1,10) == 1:    #Probability can be changed
#             island_x = team_signal[2*island_no-2]
#             island_y = team_signal[2*island_no-1]
#             team_signal = team_signal[0:start_index] + cipher(int(pirate.getID())) + team_signal[start_index+1:]
#             pirate.setTeamSignal(team_signal)
#             # pirate.moveTo(x,y,pirate)

def ActPirate(pirate):
    pirate_signal  = pirate.getSignal()
    if pirate_signal == "":
        pirate_signal = cipher(int(pirate.getID())) + " "*99
        pirate.setSignal(pirate_signal)
    updateIslandCord(pirate)
    x, y = pirate.getPosition()
    team_signal = pirate.getTeamSignal()
    status = pirate.trackPlayers()
    no_of_pirates = decipher(team_signal[9])
    for island_no in range(1,4):        #First loop to put a serpoint some tiles away and add it to team signal
        if status[island_no + 2] == "oppCapturing" and status[island_no - 1] == "myCaptured" and team_signal[5 + island_no] != " " and decipher(team_signal[5 + island_no]) != 0:
            for index in range(0,min(10,no_of_pirates//10)):
                if(team_signal[island_no*10+index] == cipher(int(pirate.getID()))):
                    island_x = ord(team_signal[2*island_no-2]) - 63
                    island_y = ord(team_signal[2*island_no-1]) - 63
                    pirate_signal = pirate.getSignal()
                    pirate_signal = pirate_signal[:3] + cipher(max(island_x-6,1)) + cipher(island_y) + pirate_signal[5:]
                    pirate_signal = pirate_signal[0] + cipher(x) + cipher(y) + pirate_signal[3:]
                    pirate.setSignal(pirate_signal)
                    # print(pirate.getID()+": ",end="")             # Testing pirate signals
                    # print(decipher(pirate_signal))
                    return moveTo(decipher(pirate_signal[3]), decipher(pirate_signal[4]), pirate)

    for island_no in range(1,4):        #Once checkpoint reached push all pirates to interior of island
        if status[island_no+2] == "oppCapturing" and status[island_no - 1] == "myCaptured" and decipher(team_signal[5 + island_no]) == 0:
            for index in range(0,min(10,no_of_pirates//10)):
                if(team_signal[island_no*10+index] == cipher(int(pirate.getID()))):
                    island_x = decipher(team_signal[2*island_no-2])
                    island_y = decipher(team_signal[2*island_no-1])
                    pirate_signal = pirate.getSignal()
                    pirate_signal = pirate_signal[:3] + cipher(island_x) + cipher(island_y) + pirate_signal[5:]
                    pirate_signal = pirate_signal[0] + cipher(x) + cipher(y) + pirate_signal[3:]
                    pirate.setSignal(pirate_signal)
                    # print(pirate.getID()+": ",end="")
                    # print(decipher(pirate_signal))
                    return moveTo(decipher(pirate_signal[3]), decipher(pirate_signal[4]), pirate)

    for island_no in range(1,4):
        island_x = team_signal[2*island_no-2]
        island_y = team_signal[2*island_no-1]
        if island_x != " " and island_y != " " and status[island_no-1] != "myCaptured":
            rand = randint(1,10)
            if rand <= 1:
                pirate_signal = pirate_signal[0] + cipher(x) + cipher(y) + pirate_signal[3:]
                pirate.setSignal(pirate_signal)
                # print(pirate.getID()+": ",end="")
                # print(decipher(pirate_signal))
                return moveTo(decipher(island_x), decipher(island_y), pirate)

    pirate_signal = pirate_signal[0] + cipher(x) + cipher(y) + pirate_signal[3:]
    pirate.setSignal(pirate_signal)
    # print(pirate.getID()+": ",end="")
    # print(decipher(pirate_signal))
    return randint(1,4)

def Closest10(team):        # Returns 10 closest pirates to defense point (max(x-6,1),y)

    team_signal = team.getTeamSignal()

    for island_no in range(1,4):
        if team_signal[2*island_no - 2] != " " and team_signal[2*island_no - 1] != " ":
            pirate_signals = team.getListOfSignals()
            island_x = max(decipher(team_signal[2*island_no - 2]) - 6,1)
            island_y = decipher(team_signal[2*island_no - 1])
            distances = {}

            for pirate_signal in pirate_signals:
                if len(pirate_signal) == 100:
                    curr_x = decipher(pirate_signal[1])
                    curr_y = decipher(pirate_signal[2])
                    pirate_id = decipher(pirate_signal[0])
                    distances[pirate_id] = abs(curr_x - island_x) + abs(curr_y - island_y)

            sorted_dist = dict(sorted(distances.items(), key=lambda item: item[1]))
            for index in range(0,min(10,len(sorted_dist))):
                team_signal = team_signal[:10*island_no + index] + cipher(list(sorted_dist)[index]) + team_signal[10*island_no + index + 1:]
            # debug = decipher(team_signal)
            team.setTeamSignal(team_signal)

# def NoOfPiratesAssembled(x ,y, team):             # Counts the numbers of points at a point
#     cnt=0
#     pirate_signals = team.getListOfSignals()
#     for pirate_signal in pirate_signals:
#         curr_x = decipher(pirate_signal[1])
#         curr_y = decipher(pirate_signal[2])
#         if curr_x == x and curr_y == y:
#             cnt += 1
#     return cnt

        
def ActTeam(team):
    deploy_x, deploy_y = team.getDeployPoint()

    team_signal = team.getTeamSignal()
    no_of_pirates = int(team.getTotalPirates())

    if team_signal == "":
        team_signal = " "*9 + cipher(no_of_pirates) + " "*90
        team.setTeamSignal(team_signal)
    
    team_signal = team_signal[:9] + cipher(no_of_pirates) + team_signal[10:]
    team.setTeamSignal(team_signal)
    Closest10(team)
    team_signal = team.getTeamSignal()
    status = team.trackPlayers()

    for island_no in range(1,4):            # Reducing frames so that defense entry is coordinated
        if status[island_no + 2] == "oppCapturing" and team_signal[5 + island_no] != " " and decipher(team_signal[5 + island_no]) != 0:
            team_signal = team_signal[:5 + island_no] + chr(ord(team_signal[5 + island_no]) - 1) + team_signal[6 + island_no:]
            team.setTeamSignal(team_signal) 

    for island_no in range(1,4):            # if Opp capturing calculating frames to assemble at common defense point
        if team_signal[2*island_no - 2] != " " and status[2 + island_no] == "oppCapturing" and status[island_no - 1] == "myCaptured" and team_signal[5 + island_no] == " ":
            island_x = decipher(team_signal[2*island_no - 2])
            island_y = decipher(team_signal[2*island_no - 1])
            pirates_defending = min(10,no_of_pirates//10)
            pirate_signals = team.getListOfSignals()
            for pirate_signal in pirate_signals:
                if pirate_signal[0] == team_signal[10*island_no + pirates_defending - 1]:
                    curr_x = decipher(pirate_signal[1])
                    curr_y = decipher(pirate_signal[2])
                    time_frames_reqd = abs(curr_x - max(island_x-6,1)) + abs(curr_y - island_y)
                    team_signal = team_signal[:5 + island_no] + cipher(time_frames_reqd) + team_signal[6 + island_no:]
                    team.setTeamSignal(team_signal)
                    break

    # debug = decipher(team_signal)

    team_signal = team.getTeamSignal()
    for island_no in range(1,4):        # Reset signal if island is defended successfully 
        if status[2 + island_no] != "oppCapturing":
            team_signal = team_signal[:5 + island_no] + " " + team_signal[6 + island_no:]
            team.setTeamSignal(team_signal)   

    team_signal = team.getTeamSignal()
    # print(decipher(team_signal))

    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)
