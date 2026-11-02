def create_player(name):
    player = {
        "name": name,
        "energy": 5,
        "location": "Beach",
        "inventory": [],
        "clues": [],
        "game_status": "running",
        "bridge_unlocked": False,
        "beacon_restored": False
    }
    return player
