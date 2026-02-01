"""
Tests for The Void Miner
"""

import unittest
from void_miner.core.game import Game


class TestGame(unittest.TestCase):
    """Test cases for the Game class"""
    
    def test_game_initialization(self):
        """Test that the game initializes correctly"""
        game = Game(width=800, height=600, fps=60)
        self.assertEqual(game.width, 800)
        self.assertEqual(game.height, 600)
        self.assertEqual(game.fps, 60)
        self.assertFalse(game.running)
        
    def test_game_custom_size(self):
        """Test game with custom size"""
        game = Game(width=1024, height=768)
        self.assertEqual(game.width, 1024)
        self.assertEqual(game.height, 768)


if __name__ == "__main__":
    unittest.main()
