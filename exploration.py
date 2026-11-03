def has_explored(player, location):
    if location in player["explored_locations"]:
        return True 
    else:
        return False 


def mark_as_explored(player, location):
    if location not in player["explored_locations"]:
        player["explored_locations"].append(location)
        return True
    
    return False


def return_to_checkpoint(player):
    checkpoint = player["checkpoint"]
    player["location"] = checkpoint


def update_checkpoint(player, location):
    player["checkpoint"] = location


