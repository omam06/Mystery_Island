player = {
    "name": "", 
    "energy": 5, 
    "location": "Beach", 
    "inventory": [], 
    "game_status": "running", 
    "clues": [], 
    "bridge_unlocked": False, 
    "beacon_restored": False
}

player_name = ""
while player_name == "":
    player_name = input("What is your name, adventurer? ").strip()
player["name"] = player_name
print(f"Hello, {player['name']}. Welcome to Mystery Island.")

valid_locations = ["Beach", "Jungle", "Cave", "Old Bridge", "Lighthouse"]
option = input("Select an option: ").strip()
if option == "1":
    locay = input("Choose where to go (Beach, Jungle, Cave, Old Bridge and Lighthouse): ").strip().title()
    if locay not in valid_locations:
        print("Location NOT in valid locations. Try again!")
    else:
        player["location"] = locay

if option == "1":
    while locay not in valid_locations:
        print("Location is invalid. Try again!")
        locay = input("Choose where to go (Beach, Jungle, Cave, Old Bridge and Lighthouse): ").strip().title()
    player["location"] = locay