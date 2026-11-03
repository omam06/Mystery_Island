valid_locations = ["Beach", "Jungle", "Cave", "Old Bridge", "Lighthouse"]

def move_player(player, destination):
    if destination not in valid_locations:
        return False
    elif destination == player["location"]:
        return False 
    elif destination == "Old Bridge" and "Key" not in player["inventory"]:
        return False
    elif destination == "Lighthouse" and (not player["bridge_unlocked"] or "Lantern" not in player["inventory"]):
        return False
    else:
        player["location"] = destination
        return True 

def unlock_bridge(player):
    if player["bridge_unlocked"]:
        print("Bridge has been unlocked. Go right on!")
        return True
    elif "Key" not in player["inventory"]:
        print("You need a key to unlock the bridge")
        return False
    else:
        player["bridge_unlocked"] = True
        print("You successfully unlocked the bridge!")
        return True
    