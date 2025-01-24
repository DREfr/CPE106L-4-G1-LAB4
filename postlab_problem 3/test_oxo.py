import unittest
from oxo_logic import newGame, userMove, computerMove, _isWinningMove, _generateMove
from oxo_data import saveGame, restoreGame
import os
from unittest.mock import patch

class TestOXO(unittest.TestCase):

    # Testing new game
    def test_new_game(self):
        # Test that a new game initializes with 9 empty spaces
        game = newGame()
        self.assertEqual(game, [' '] * 9)

    # Testing save and restore game
    @patch('oxo_data._getPath')
    def test_save_and_restore_game(self, mock_getPath):
        # Mock the file path to avoid file system dependency
        mock_getPath.return_value = os.getcwd()

        game = ['X', 'O', ' ', ' ', 'X', ' ', 'O', ' ', 'X']
        saveGame(game)

        # Now test if the game is saved and restored correctly
        restored_game = restoreGame()
        self.assertEqual(game, restored_game)

    # Testing generate move (of bot)
    @patch('random.choice')
    def test_generate_move(self, mock_random_choice):
        # Test that the computer generates a valid move
        game = newGame()
        mock_random_choice.return_value = 4  # Mocking random choice to return 4
        move = _generateMove(game)
        self.assertEqual(move, 4)  # Bot should choose position 4

    # Testing the winning move
    def test_is_winning_move(self):
        # Test winning condition detection
        game = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertTrue(_isWinningMove(game))

    # Testing the user's movement
    def test_user_move_valid(self):
        # Test that a user move updates the game correctly
        game = newGame()
        result = userMove(game, 0)  # User plays at position 0
        self.assertEqual(game[0], 'X')
        self.assertEqual(result, "")

    def test_user_move_invalid(self):
        # Test that an invalid move raises an exception
        game = newGame()
        userMove(game, 0)  # First move
        with self.assertRaises(ValueError):
            userMove(game, 0)  # Second move on the same cell should raise error

    # Testing the bot's (opponent's) movement
    def test_computer_move(self):
        # Test that computer makes a valid move
        game = newGame()
        result = computerMove(game)
        self.assertIn('O', game)
        self.assertIn(result, ["", "O", "D"])

    @patch('random.choice')
    def test_computer_move_random(self, mock_random_choice):
        # Test that the computer makes a random valid move
        game = newGame()
        mock_random_choice.return_value = 4  # Mocking random choice to return 4
        result = computerMove(game)
        self.assertEqual(game[4], 'O')  # Computer should play at position 4


if __name__ == '__main__':
    unittest.main()
