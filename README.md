# Mystery_Island

## About the Project

Mystery Island is a command-line adventure game built with Python. The player wakes up on a mysterious island after a terrible storm and must explore different locations, collect useful items, solve puzzles, and restore a lighthouse beacon to signal a rescue ship.

Players must manage their energy carefully because wrong decisions and failed puzzles can reduce their chances of escaping the island.

## Features

- **Five locations:** Beach, Jungle, Cave, Old Bridge, and Lighthouse.
- **Energy system:** Players start with 5 energy points. Risky decisions and incorrect puzzle answers can reduce their energy.
- **Inventory system:** Collect useful items such as the Lantern and Key.
- **Exploration:** Discover clues, solve puzzles, and unlock new areas.
- **Checkpoint system:** Return to the latest checkpoint after certain failed challenges.
- **Lighthouse puzzle:** Discover three clues and activate the switches in the correct order to restore the beacon.
- **Win and lose conditions:** Escape by restoring the beacon or lose when energy reaches zero.
- **Replay option:** Start a fresh game after winning, losing, or quitting.

## Requirements

- Python 3.10 or later.
- No external libraries are required. The game uses Python's standard library.

## Project Structure

```
Mystery_Island/
│
├── main.py
├── game_state.py
├── movement.py
├── energy.py
├── inventory.py
├── clues.py
├── exploration.py
│
└── tests/
    ├── __init__.py
    ├── test_game_state.py
    ├── test_movement.py
    ├── test_energy.py
    ├── test_inventory.py
    ├── test_clues.py
    └── test_exploration.py
```

## How to Run

1. Make sure Python is installed on your computer.
2. Open a terminal in the `Mystery_Island` project directory.
3. Run:

```bash
python main.py
```

On some systems, you may need:

```bash
python3 main.py
```

## How to Play

1. Enter your name to begin the adventure.
2. Read the introductory clue and make your first decision.
3. Use the main menu to explore locations, travel, check your inventory, view your status, or quit.
4. Solve the Jungle and Cave puzzles to collect useful items.
5. Use the Key to unlock the Old Bridge.
6. Enter the Lighthouse with the required items.
7. Search all three Lighthouse rooms to discover the clues.
8. Activate the switches in the correct order:
   - Power
   - Signal
   - Beacon
9. Restore the beacon to signal the rescue ship and win the game.

**Important rules:**
- Players start with 5 energy points.
- Energy is deducted for risky decisions and incorrect puzzle answers.
- Reaching zero energy ends the game.
- Ordinary movement between locations does not cost energy.
- Collected items and discovered clues are retained when returning to a checkpoint.
- Completed locations cannot be explored repeatedly to collect the same rewards.

## Running the Tests

The project includes unit tests for its main game modules.

From the project directory, run:

```bash
python -m unittest discover -s tests -v
```

Or, depending on your system:

```bash
python3 -m unittest discover -s tests -v
```

## Known Limitations

- The game runs entirely in the terminal; it does not have a graphical interface.
- Player progress is not saved after the program closes.
- The game is designed for single-player use.
- Puzzle answers are based on predefined expected answers rather than advanced natural-language interpretation.