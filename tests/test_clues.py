import unittest
from game_state import create_player
from clues import discover_clue


class TestClues(unittest.TestCase):

    def test_discover_new_clue(self):
        player = create_player("Como")
        add_clue = discover_clue(player, "lighthouse inscription")
        self.assertTrue(add_clue)
        self.assertIn("lighthouse inscription", player["clues"])

    def test_cannot_discover_same_clue_twice(self):
        player = create_player("Como")
        discover_clue(player, "lighthouse inscription")
        clue2 = discover_clue(player, "lighthouse inscription")
        self.assertFalse(clue2)
        self.assertEqual(player["clues"].count("lighthouse inscription"), 1)

    def test_discover_different_clues(self):
        player = create_player("Como")
        discover_clue(player, "lighthouse inscription")
        discover_clue(player, "strange footprints")
        self.assertIn("lighthouse inscription", player["clues"])
        self.assertIn("strange footprints", player["clues"])
        self.assertEqual(len(player["clues"]), 2)