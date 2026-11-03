from game_state import create_player
from energy import use_energy
from exploration import has_explored, mark_as_explored, update_checkpoint, return_to_checkpoint
from clues import discover_clue
from movement import move_player
from inventory import collect_item

print("======== MYSTERY ISLAND: MAKE IT OUT OR DIE TRYING ========\n")
name = input("Hello, Adventurer, What is your name? ").strip()
player = create_player(name)
print(f"\nWelcome, {name}. You wake up on a mysterious island after a terrible storm. Try to find your way out and try not to die while at it. Good luck, you'll need it around here.\n")

intro_clue = "The lighthouse beacon must be restored for help to come."
print(f"INTRODUCTORY CLUE: {intro_clue}")
discover_clue(player, intro_clue)

print("\n--You notice a suspicious trail leading away from your position on the beach--")
print("You have 2 options:")
print("1. Follow")
print("2. Ignore\n")

choice = input("Enter an option: ").strip()
while choice != "1" and choice != "2":
    print("Invalid option. Try again!")
    choice = input("Enter an option: ").strip()

if choice == "1":
    print("A massive wild boar suddenly emerges from the bushes, startling you. You managed to escape to safety but the encounter costs you some energy.")
    use_energy(player)

else:
    print("Suspicious trail ignored. Continue your adventure away from the beach.")

if player["game_status"] == "lost":
    print("Oh snap X, You ran out of energy. Game over!")
else:
    print("\nNice job, Adventurer. You survived this phase. Continue exploring.")
    mark_as_explored(player, "Beach")

    
    while player["game_status"] == "running":
        print("\n----- MAIN MENU -----")
        print("1. Explore current location")
        print("2. Travel to another location")
        print("3. Check inventory")
        print("4. Check player status")
        print("5. Quit game")
        menu_choice = input("Select an option: ").strip()

        if menu_choice == "1":
            pass

        elif menu_choice == "2":
            print("\nAVAILABLE LOCATIONS")
            print("1. Beach")
            print("2. Jungle")
            print("3. Cave")
            print("4. Old Bridge")
            print("5. Lighthouse")
            locations = {"1": "Beach", "2": "Jungle", "3": "Cave", "4": "Old Bridge", "5": "Lighthouse"}
            where = input("Select your preferred destination: ").strip()
            if where in locations:
                motion = locations[where]
                locomotion = move_player(player, motion)
                if locomotion:
                    print("\nMovement succeeded.")
                else:
                    print("Oh, snap! Movement failed.")
            else:
                print("Invalid destination. Must be from 1 to 5")


        elif menu_choice == "3":
            print("YOUR INVENTORY")
            if len(player["inventory"]) == 0:
                print("Inventory is empty")
            else:
                print(player["inventory"])
                    
        elif menu_choice == "4":
            print(f"Name: {player['name']}")
            print(f"Current Location: {player['location']}")
            print(f"Total Energy: {player['energy']}")
            print(f"List of Inventory: {player['inventory']}")
            print(f"Discovered Clues: {player['clues']}")
            print(f"Locations Successfully Explored: {player['explored_locations']}")
            print(f"Last saved checkpoint: {player['checkpoint']}")


        elif menu_choice == "5":
            print("Thanks for playing Mystery Island. Goodbye!")
            player["game_status"] = "exit"
        
        else:
            print("Invalid option. Try again!")