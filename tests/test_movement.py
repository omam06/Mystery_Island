import unittest
from game_state import create_player
from movement import move_player

class TestMovement(unittest.TestCase):
    
    def test_valid_destination_not_current_location(self):
        player = create_player("Metro")
        movement = move_player(player, "Cave")
        self.assertTrue(movement)
        self.assertEqual(player["location"], "Cave")

    def test_invalid_destination_does_not_change_location(self):
        player = create_player("Metro")
        movement = move_player(player, "Boat")
        self.assertFalse(movement)
        self.assertEqual(player["location"], "Beach")

    def test_trying_to_move_to_current_location_fails(self):
        player = create_player("Metro")
        movement = move_player(player, "Beach")
        self.assertFalse(movement)
        self.assertEqual(player["location"], "Beach")