import unittest
from game_state import create_player
from inventory import collect_item

class TestInventory(unittest.TestCase):

    def test_collect_new_item(self):
        player = create_player("Imor")
        collection = collect_item(player, "rope")
        self.assertTrue(collection)
        self.assertIn("rope", player["inventory"])

    def test_cannot_collect_same_item_twice(self):
        player = create_player("Imor")
        collect_item(player, "lantern")
        collection2 = collect_item(player, "lantern")
        self.assertFalse(collection2)
        self.assertEqual(player["inventory"].count("lantern"), 1)

    def test_collect_different_items(self):
        player = create_player("Imor")
        collect_item(player, "rope")
        collect_item(player, "lantern")
        self.assertIn("rope", player["inventory"])
        self.assertIn("lantern", player["inventory"])
        self.assertEqual(len(player["inventory"]), 2)