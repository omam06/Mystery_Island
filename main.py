from game_state import create_player
from energy import use_energy
from exploration import has_explored, mark_as_explored, update_checkpoint, return_to_checkpoint
from clues import discover_clue
from movement import move_player
from inventory import collect_item

name = input("Hello, Adventurer, What is your name? ").strip()
player = create_player(name)
print(f"Welcome, {name}. You wake up on a mysterious island after a terrible storm. Try to find your way out and try not to die while at it. Good luck, you'll need it around here.")
