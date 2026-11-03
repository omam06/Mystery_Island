def collect_item(player, item):
    if item in player["inventory"]:
        return False
    
    player["inventory"].append(item)
    return True