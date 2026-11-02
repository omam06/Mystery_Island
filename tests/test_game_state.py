import unittest
from game_state import create_player

class TestGameState(unittest.TestCase):
    
    def test_player_starts_with_five_energy(self):
        player = create_player("Key Glock")
        self.assertEqual(player["energy"], 5)

    def test_player_name(self):
        player = create_player("Keith")
        self.assertEqual(player["name"], "Keith")
    
    def test_player_starts_at_beach(self):
        player = create_player("Keith")
        self.assertEqual(player["location"], "Beach")

    def test_player_inventory_start_empty(self):
        player = create_player("Keith")
        self.assertEqual(player["inventory"], [])

    def test_player_clues_start_empty(self):
        player = create_player("Keith")
        self.assertEqual(player["clues"], [])

    def test_bridge_starts_locked(self):
        player = create_player("Keith")
        self.assertFalse(player["bridge_unlocked"])

    def test_beacon_starts_unrestored(self):
        player = create_player("Keith")
        self.assertFalse(player["beacon_restored"])

    def test_game_starts_running(self):
        player = create_player("Keith")
        self.assertEqual(player["game_status"], "running")