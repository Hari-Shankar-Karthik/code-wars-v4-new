from utils.cipher import *
from utils.decipher import *

def ClosestN(team, x, y, N):        #Returns list of decipher closest N pirates to a point. Need to cipher it if using for team signal

    x = int(x)
    y = int(y)
    distances = {}

    for pirate_signal in pirate_signals:
        if len(pirtae_signal) == 100:
            curr_x = decipher(pirate_signal[1])
            curr_y = decipher(pirate_signal[2])
            pirate_id = decipher(pirate_signal[0])
            distances[pirate_id] = abs(curr_x - x) + abs(curr_y - y)
    
    sorted_dist = dict(sorted(distances.items(), key=lambda item: item[1]))
    l = []

    for index in range(0,N):
        l.append(list(sorted_dist)[index])

    return l