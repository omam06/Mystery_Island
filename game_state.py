def create_player(name):
    player = {
        "name": name,
        "energy": 5,
        "location": "Beach",
        "explored_locations": [],
        "checkpoint": "Beach",
        "lighthouse_room": None,
        "searched_lighthouse_rooms": [],
        "inventory": [],
        "clues": [],
        "game_status": "running",
        "bridge_unlocked": False,
        "beacon_restored": False
    }
    return player
