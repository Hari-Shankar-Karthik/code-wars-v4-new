from random import randint

from utils.pirate_movements import moveTo, moveAway
# from utils.defend_island import defend_island

# TEAM SIGNAL FORMAT:
# "x1y1x2y2x3y3abcdef"
# x1, y1, x2, y2, x3, y3 are the coordinates of the islands. 
# If not known, they are "  " (2 spaces).
# If they are a single digit, they are followed by a space. (IMPORTANT)
# a: should be "1" if island 1 is to be attacked and " " if not.
# b: should be "2" if island 2 is to be attacked and " " if not.
# c: should be "3" if island 3 is to be attacked and " " if not.
# d: should be "1" if island 1 is to be defended and " " if not.
# e: should be "2" if island 2 is to be defended and " " if not.
# f: should be "3" if island 3 is to be defended and " " if not.

# PIRATE SIGNAL FORMAT:
# "S" - Scout
# "Ax" - Attacker for island x (x = 1, 2, 3)
# "Dx" - Defender for island x (x = 1, 2, 3)
# "P" - Passive Scout

# TODO: POINTS TO REVIEW:
# -> Movement of the attacker on an island
# -> Splitting (or not) of defenders when two islands are attacked at the same time
# -> Movement (or not) of defenders when an island is attacked (inside/outside, etc.)
# -> Percentage chance of scout becoming attacker vs. passive scout when an attack command is given
# -> Movement of the scout (always away from the deploy point, or different origin?)

name = "my_script"

def ActPirate(pirate):

    # newly created pirates are set to Scout by default
    if pirate.getSignal() == "":
        pirate.setSignal("S")
    
    pirate_signal = pirate.getSignal()
    team_signal = pirate.getTeamSignal()

    if pirate_signal == "S":
        current_location = pirate.investigate_current()[0]
        track = pirate.trackPlayers()

        # the scout first checks if he is on an island which is either neutral or enemy
        # if it is, he becomes of type Attacker
        if current_location.startswith("island") and track[int(current_location[-1]) - 1] != "myCaptured":
            pirate_signal = f"A{current_location[-1]}"
            pirate.setSignal(pirate_signal)
            
            # store this island's location in the team signal
            island_number = int(current_location[-1])
            island_x, island_y = pirate.getPosition()
            # island 1's coords are stored in indices 0,1 and 2,3
            # island 2's coords are stored in indices 4,5 and 6,7
            # island 3's coords are stored in indices 8,9 and 10,11

            def stringify(num):
                num = str(num)
                if len(num) == 1:
                    return num + " "
                return num
            
            def update(arr, index, value):
                arr[index] = value[0]
                arr[index + 1] = value[1]

            team_signal = list(team_signal)
            update(team_signal, island_number * 4 - 4, stringify(island_x))
            update(team_signal, island_number * 4 - 2, stringify(island_y))
            
            # store "attack this island" on the team signal if not already done
            # 12, 13 and 14 are the indices of attack commands for islands 1, 2 and 3 respectively in the team signal
            team_signal[island_number + 11] = str(island_number)
            
            # convert the list back to string and update the team signal
            team_signal = "".join(team_signal)
            pirate.setTeamSignal(team_signal)

            # TODO: attacker should not just stay on one spot, but should move around the island
            return 0 # temporary measure
        
        # next, the scout checks the team signal to become defender
        # if two islands are attacked at the same time, defenders DON'T split (TODO: review this)
        # 15, 16 and 17 are the indices of defence commands for islands 1, 2 and 3 respectively in the team signal
        if team_signal[15] != " ":
            pirate_signal = "D1"
        elif team_signal[16] != " ":
            pirate_signal = "D2"
        elif team_signal[17] != " ":
            pirate_signal = "D3"
        else:
            for i in [1, 2, 3]:
                if track[i - 1] == "myCaptured" and track[i + 2] == "oppCapturing":
                    pirate_signal = f"D{i}"
                    break
        if pirate_signal[0] == "D":
            pirate.setSignal(pirate_signal)
            # TODO: movement of defender: review whether is it required, how to move, etc.
            return 0 # temporary measure
        
        # next, the scout checks whether there is an attack command on the team signal
        # if there is, he has the chance to become Attacker
        # 12, 13 and 14 are the indices of attack commands for islands 1, 2 and 3 respectively in the team signal
        # TODO: IMPLEMENT PERCENTAGE-WISE chances of becoming attacker vs. passive scout
        if team_signal[12] != " ":
            pirate_signal = "A1"
        elif team_signal[13] != " ":
            pirate_signal = "A2"
        elif team_signal[14] != " ":
            pirate_signal = "A3"
        
        if pirate_signal[0] == "A":
            pirate.setSignal(pirate_signal)
            # TODO: movement of attacker: review whether is it required, how to move, etc.
            return 0 # temporary measure
        
        # if none of the above conditions are met, the scout explores
        # TODO: review whether to change the origin from which moveAway happens
        deploy_x, deploy_y = pirate.getDeployPoint()
        return moveAway(deploy_x, deploy_y, pirate)
    
    elif pirate_signal[0] == "A":
        island_number = int(pirate_signal[1])
        island_x, island_y = pirate.getPosition()
        # 0, 1 and 2 are the indices of the coordinates of islands 1, 2 and 3 respectively in the team signal
        # 3, 4 and 5 are the indices of attack commands for islands 1, 2 and 3 respectively in the team signal
        if team_signal[island_number * 4 - 4] != " ":
            team_signal = list(team_signal)
            team_signal[island_number * 4 - 4] = "  "
            team_signal[island_number * 4 - 3] = "  "
            team_signal[island_number + 11] = " "
            team_signal = "".join(team_signal)
            pirate.setTeamSignal(team_signal)
            pirate.setSignal("S")
            return 0
        
        

def ActTeam(team):
    pass