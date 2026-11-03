def discover_clue(player, clue):
    if clue in player["clues"]:
        return False
    
    player["clues"].append(clue)
    return True