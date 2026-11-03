import unittest
from game_state import create_player
from exploration import has_explored, mark_as_explored, return_to_checkpoint, update_checkpoint

class TestExploration(unittest.TestCase):

    def test_already_explored_location_returns_true(self):
        player = create_player("Tony")
        player["explored_locations"] = ["Beach"]
        go_again = has_explored(player, "Beach")
        self.assertTrue(go_again)

    def test_location_not_yet_explored_returns_false(self):
        player = create_player("Tony")
        player["explored_locations"] = ["Jungle"]
        explore_now = has_explored(player, "Cave")
        self.assertFalse(explore_now)

    def test_empty_exploration_list(self):
        player = create_player("Tony")
        empty_list = has_explored(player, "Jungle")
        self.assertFalse(empty_list)

    def test_mark_new_location_as_explored(self):
        player = create_player("Tony")
        mark_as_explored(player, "Beach")
        self.assertIn("Beach", player["explored_locations"])
    
    def test_already_explored_location_not_duplicated(self):
        player = create_player("Tony")
        player["explored_locations"] = ["Cave"]
        mark_as_explored(player, "Cave")
        self.assertEqual(player["explored_locations"].count("Cave"), 1)

    def test_returns_player_to_checkpoint(self):
        player = create_player("Tony")
        player["location"] = "Jungle"
        return_to_checkpoint(player)
        self.assertEqual(player["location"], "Beach")
        self.assertEqual(player["energy"], 5)

    def test_does_not_change_checkpoint(self):
        player = create_player("Tony")
        return_to_checkpoint(player)
        self.assertEqual(player["checkpoint"], "Beach")
    def test_updates_checkpoint(self):
        player = create_player("Tony")
        update_checkpoint(player, "Jungle")
        self.assertEqual(player["checkpoint"], "Jungle")

    def test_does_not_change_current_location(self):
        player = create_player("Tony")
        update_checkpoint(player, "Cave")
        self.assertEqual(player["location"], "Beach")