import unittest
from game_state import create_player
from movement import move_player, unlock_bridge

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

    def test_cannot_enter_old_bridge_without_key(self):
        player = create_player("Metro")
        movement = move_player(player, "Old Bridge") 
        self.assertFalse(movement)
        self.assertEqual(player["location"], "Beach")
    
    def test_movement_to_lighthouse_fails_if_bridge_still_locked(self):
        player = create_player("Metro")
        player["inventory"].append("Lantern")

        movement = move_player(player, "Lighthouse")
        self.assertFalse(movement)
        self.assertEqual(player["location"], "Beach")

    def test_cannot_move_to_lighthouse_if_bridge_unlocked_but_no_lantern(self):
        player = create_player("Metro")
        player["bridge_unlocked"] = True

        movement = move_player(player, "Lighthouse")
        self.assertFalse(movement)
        self.assertEqual(player["location"], "Beach")

    def test_move_to_lighthouse_if_both_requirements_are_satisfied(self):
        player = create_player("Metro")
        player["bridge_unlocked"] = True 
        player["inventory"].append("Lantern")

        movement = move_player(player, "Lighthouse")
        self.assertEqual(player["location"], "Lighthouse")
        self.assertTrue(movement)

    def test_unlocking_bridge_with_key(self):
        player = create_player("Metro")
        player["inventory"].append("Key")
        result = unlock_bridge(player)
        self.assertTrue(result)
        self.assertEqual(player["bridge_unlocked"], True)

    def test_cannot_unlock_bridge_without_key(self):
        player = create_player("Metro")
        result = unlock_bridge(player)
        self.assertFalse(result) 
        self.assertEqual(player["bridge_unlocked"], False)

    def test_bridge_already_unlocked(self):
        player = create_player("Metro")
        player["bridge_unlocked"] = True 
        result = unlock_bridge(player)
        self.assertTrue(result)
        self.assertEqual(player["bridge_unlocked"], True)