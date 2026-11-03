import unittest
from game_state import create_player
from energy import use_energy

class TestEnergy(unittest.TestCase):

    def test_energy_reduces_by_one(self):
        player = create_player("Jasper")
        use_energy(player)
        self.assertEqual(player["energy"], 4)
        self.assertEqual(player["game_status"], "running")

    def test_energy_reaching_zero_ends_game(self):
        player = create_player("Jasper")
        player["energy"] = 1
        use_energy(player)
        self.assertEqual(player["energy"], 0)
        self.assertEqual(player["game_status"], "lost")

    def test_energy_does_not_reduce_after_game_over(self):
        player = create_player("Jasper")
        player["energy"] = 0
        player["game_status"] = "lost"
        use_energy(player)
        self.assertEqual(player["energy"], 0)
        self.assertEqual(player["game_status"], "lost") 