import unittest
import RPS_game

class TestRPS(unittest.TestCase):
    def test_draw(self):
        self.assertEqual(RPS_game.get_winner("rock", "rock"), "Draw")
        self.assertEqual(RPS_game.get_winner("paper", "paper"), "Draw")
        self.assertEqual(RPS_game.get_winner("scissors", "scissors"), "Draw")

    def test_player_wins(self):
        self.assertEqual(RPS_game.get_winner("rock", "scissors"), "Player")
        self.assertEqual(RPS_game.get_winner("paper", "rock"), "Player")
        self.assertEqual(RPS_game.get_winner("scissors", "paper"), "Player")

    def test_computer_wins(self):
        self.assertEqual(RPS_game.get_winner("rock", "paper"), "Computer")
        self.assertEqual(RPS_game.get_winner("paper", "scissors"), "Computer")
        self.assertEqual(RPS_game.get_winner("scissors", "rock"), "Computer")

    def test_invalid_choice(self):
        with self.assertRaises(ValueError):
            RPS_game.play("invalid")

if __name__ == "__main__":
    unittest.main()
