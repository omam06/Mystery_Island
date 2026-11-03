valid_locations = ["Beach", "Jungle", "Cave", "Old Bridge", "Lighthouse"]

def move_player(player, destination):
    if destination not in valid_locations:
        return False
    elif destination == player["location"]:
        return False 
    else:
        player["location"] = destination
        return True 