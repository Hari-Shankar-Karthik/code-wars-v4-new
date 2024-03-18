def ActPirate(pirate):
    up = pirate.investigate_up()[0]
    ne = pirate.investigate_ne()[0]
    nw = pirate.investigate_nw()[0]
    down = pirate.investigate_down()[0]
    se = pirate.investigate_se()[0]
    sw = pirate.investigate_sw()[0]
    right = pirate.investigate_right()[0]
    left = pirate.investigate_left()[0]
    x, y = pirate.getPosition()

    if (
        (up == "island1" and s[0] != "myCaptured")
        or (up == "island2" and s[1] != "myCaptured")
        or (up == "island3" and s[2] != "myCaptured")
    ):
        if (up == ne and up == nw):
            s = up[-1] + str(x) + "," + str(y - 2)
        elif (up == ne):
            s = up[-1] + str(x+1) + "," + str(y - 2)
        else:
            s = up[-1] + str(x-1) + "," + str(y - 2)

        if(island_cord[int(s[0])] == ""):
            island_cord[int(s[0])] = s[1:]

    elif (
        (down == "island1" and s[0] != "myCaptured")
        or (down == "island2" and s[1] != "myCaptured")
        or (down == "island3" and s[2] != "myCaptured")
    ):
        if (down == se and down == sw):
            s = down[-1] + str(x) + "," + str(y + 2)
        elif (down == se):
            s = down[-1] + str(x-1) + "," + str(y + 2)
        else:
            s = down[-1] + str(x+1) + "," + str(y + 2)

        if(island_cord[int(s[0])] == ""):
            island_cord[int(s[0])] = s[1:]

    elif (
        (left == "island1" and s[0] != "myCaptured")
        or (left == "island2" and s[1] != "myCaptured")
        or (left == "island3" and s[2] != "myCaptured")
    ):
        if (left == nw and left == sw):
            s = left[-1] + str(x - 2) + "," + str(y)
        elif (left == nw):
            s = left[-1] + str(x - 2) + "," + str(y-1)
        else:
            s = left[-1] + str(x - 2) + "," + str(y+1)

        if(island_cord[int(s[0])] == ""):
            island_cord[int(s[0])] = s[1:]

    elif (
        (right == "island1" and s[0] != "myCaptured")
        or (right == "island2" and s[1] != "myCaptured")
        or (right == "island3" and s[2] != "myCaptured")
    ):
        if(right == ne and right == se):
            s = right[-1] + str(x + 2) + "," + str(y)
        elif(right == ne):
            s = right[-1] + str(x + 2) + "," + str(y-1)
        else:
            s = right[-1] + str(x + 2) + "," + str(y+1)

        if(island_cord[int(s[0])] == ""):
            island_cord[int(s[0])] = s[1:]
    
    elif (
        (ne == "island1" and s[0] != "myCaptured")
        or (ne == "island2" and s[1] != "myCaptured")
        or (ne == "island3" and s[2] != "myCaptured")
    ):
        s = ne[-1] + str(x + 2) + "," + str(y-2)
        if(island_cord[int(s[0])] == ""):
            island_cord[int(s[0])] = s[1:]

    elif (
        (se == "island1" and s[0] != "myCaptured")
        or (se == "island2" and s[1] != "myCaptured")
        or (se == "island3" and s[2] != "myCaptured")
    ):
        s = se[-1] + str(x + 2) + "," + str(y+2)
        if(island_cord[int(s[0])] == ""):
            island_cord[int(s[0])] = s[1:]

    elif (
        (nw == "island1" and s[0] != "myCaptured")
        or (nw == "island2" and s[1] != "myCaptured")
        or (nw == "island3" and s[2] != "myCaptured")
    ):
        s = nw[-1] + str(x - 2) + "," + str(y-2)
        if(island_cord[int(s[0])] == ""):
            island_cord[int(s[0])] = s[1:]

    elif (
        (sw == "island1" and s[0] != "myCaptured")
        or (sw == "island2" and s[1] != "myCaptured")
        or (sw == "island3" and s[2] != "myCaptured")
    ):
        s = sw[-1] + str(x - 2) + "," + str(y + 2)
        if(island_cord[int(s[0])] == ""):
            island_cord[int(s[0])] = s[1:]

def ActTeam(team):
    pass