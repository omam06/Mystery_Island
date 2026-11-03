def use_energy(player):
    if player["game_status"] != "running":
            return
    
    energy_left = player["energy"] - 1
    player["energy"] = energy_left
    
    if player["energy"] == 0:
        player["game_status"] = "lost"
    