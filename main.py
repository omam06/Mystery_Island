from game_state import create_player
from energy import use_energy
from exploration import has_explored, mark_as_explored, update_checkpoint, return_to_checkpoint
from clues import discover_clue
from movement import move_player, unlock_bridge
from inventory import collect_item

lighthouse_clues = {
    "Control Room": "The power switch must be activated first.",
    "Storage Room": "The signal switch must be activated second.",
    "Beacon Room": "The beacon switch must be activated last."
}

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
            if player["location"] == "Old Bridge":
                print("You stand before the Old Bridge")
                print("\nYou have 2 options:")
                print("1. Use key to unlock the bridge")
                print("2. Return to the main menu")
                oldbridge_choice = input("\nSelect one: ").strip()
                while oldbridge_choice != "1" and oldbridge_choice != "2":
                    print("Invalid option. Try again!")
                    oldbridge_choice = input("\nSelect one: ").strip()
                                                        
                if oldbridge_choice == "1":
                    unlock_bridge(player)
                    
                elif oldbridge_choice == "2":
                    print("Returning to main menu....")

            elif player["location"] == "Jungle":
                if has_explored(player, "Jungle"):
                    print("Jungle has been explored. You may only return here as checkpoint, not to explore again.")
                else:
                    print("\nYou've entered the Jungle. Two paths lie ahead:")
                    print("1. Take the rocky shortcut (costs 1 energy)")
                    print("2. Take the longer, safer route (no energy cost)")
                    jungle_choice = input("Select your choice: ").strip()
                    while jungle_choice != "1" and jungle_choice != "2":
                        print("Invalid option. Try again!")
                        jungle_choice = input("Select your choice: ").strip()
                
                    if jungle_choice == "1":
                        use_energy(player)

                    if player["game_status"] == "running":
                        print("\nYou discover 3 sets of animal footprints:")
                        print("\nRabbit: paired prints.")
                        print("Deer: split-hoof prints")
                        print("Elephant: large round footprints.\n")
                        print("Arrange the animals from smallest to largest.")
                        
                        answer = input("Enter your order with first letters in capital, separated by commas: ").strip()
                        if answer == "Rabbit, Deer, Elephant":
                            print("\nCongrats! You opened the chest.")
                            collect_item(player, "Lantern")
                            print("Lantern collected successfully")
                            mark_as_explored(player, "Jungle")
                            print("You completely explored the Jungle. Great Adventurer, you are.")
                            update_checkpoint(player, "Jungle")
                        else:
                            print("Oh Snap! That's an incorrect order.")
                            use_energy(player)
                            if player["game_status"] == "running":
                                return_to_checkpoint(player)
                                print(f"You have been returned to your last saved checkpoint; The {player['checkpoint']}")

            elif player["location"] == "Cave":
                if has_explored(player, "Cave"):
                    print("Cave already explored. You cannot explore it again.")
                else:
                    print("\nYou hear a strange sound coming from another section of the Cave.")
                    print("You have two options:")
                    print("1. Investigate the sound")
                    print("2. Ignore it")

                    cave_choice = input("Select an option: ").strip()
                    while cave_choice != "1" and cave_choice != "2":
                        print("Invalid option. Try again!")
                        cave_choice = input("Select an option: ").strip()

                    if cave_choice == "1":
                        print("\nYou cautiously investigate the sound...")
                        print("A wild animal suddenly appears. You escape safely, but lose 1 energy.")
                        use_energy(player)

                        if player["game_status"] == "running":
                            inscription = "Some things have teeth, yet never eat. They are made to open what is closed."
                            print(f"While escaping, you discover an inscription: {inscription}")
                            discover_clue(player, inscription)
                    else:
                        print("\nYou decide to ignore the sound and continue exploring.")

                    if player["game_status"] == "running":
                        print("\nYou discover an old locked container")
                        print("An inscription on it reads:")
                        print(' "I have teeth but cannot bite. Open doors but have no hands." ')

                        riddle_answer = input("What am I? ").strip()

                        if riddle_answer == "Key":
                            print("\nCorrect! The container unlocks.")
                            collect_item(player, "Key")
                            print("Key collected successfully!")

                            mark_as_explored(player, "Cave")
                            update_checkpoint(player, "Cave")
                            print("Adventurer. You completely explored the cave!")
                        else:
                            print("\nOh snap! Incorrect answer. You lose 1 energy.")
                            use_energy(player)

                            if player["game_status"] == "running":
                                return_to_checkpoint(player)
                                print(f"You have been returned to your last saved checkpoint: The {player['checkpoint']}")

            elif player["location"] == "Lighthouse":
                print(f"\nYou are now in the {player['lighthouse_room']}")

                print("\nLIGHTHOUSE MENU")
                print("1. Search this room")
                print("2. Move to another room")
                print("3. View discovered clues")
                print("4. Leave Lighthouse")

                house_choice = input("Select an option: ").strip()
                if house_choice == "1":
                    current_room = player["lighthouse_room"]

                    if current_room in player["searched_lighthouse_rooms"]:
                        print("\nYou already searched this room. Nothing else to find.")
                    else:
                        clue = lighthouse_clues[current_room]
                        discover_clue(player, clue)
                        player["searched_lighthouse_rooms"].append(current_room)

                        print("\nYou discovered a clue!")
                        print(clue)
                elif house_choice == "2":
                    rooms = {"1": "Control Room", "2": "Storage Room", "3": "Beacon Room"}
                    print("\nRooms in the Lighthouse:")
                    print("1. Control Room")
                    print("2. Storage Room")
                    print("3. Beacon Room")
                    
                    room_choice = input("Select a room to enter: ").strip()
                    while room_choice != "1" and room_choice != "2" and room_choice !="3":
                        print("Invalid room number. Try again!")
                        room_choice = input("Select a room to enter: ").strip()

                    if room_choice in rooms:
                        barge_in = rooms[room_choice]
                        player["lighthouse_room"] = barge_in
                        print(f"\nYou have moved to the {player['lighthouse_room']}")

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
                if motion == "Lighthouse" and "Lantern" not in player["inventory"]:
                    print("\nYou cannot enter the Lighthouse without a Lantern")
                    print("You lose 1 energy")
                    use_energy(player)

                    if player["game_status"] == "running":
                        player["location"] = "Jungle"
                        print("You have been sent back to the Jungle. Find the Lantern!")

                elif move_player(player, motion):
                    print(f"\nMovement succeeded. Current location: The {motion}")
                    
                    if motion == "Lighthouse":
                        player["lighthouse_room"] = "Control Room"
                        print("You have entered the Lighthouse Control Room")
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

    if player["game_status"] == "lost":
        print("\nYour energy has run out. You couldn't survive the island.")
        print("GAME OVER! Thanks for playing Mystery Island.")