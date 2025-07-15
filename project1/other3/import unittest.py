import unittest
from unittest.mock import patch
from mainfucntionVariant import play_game

class TestPlayGame(unittest.TestCase):

    @patch('your_game_file.display_menu')
    @patch('your_game_file.get_computer_choice', return_value='rock')
    @patch('your_game_file.get_user_choice', side_effect=['rock', 'q'])
    @patch('your_game_file.determine_winner')
    def test_play_game_quit_immediately(self, mock_winner, mock_user_choice, mock_computer_choice, mock_menu):
        """
        1. Test case description: Test if the game quits immediately when the user inputs 'q'.
        Expected outcome: The game loop should break, and "Thanks for playing!" should be printed.
        """
        with self.assertLogs(level='INFO') as log:
            play_game()
            self.assertIn("Thanks for playing!", log.output[0])

    @patch('your_game_file.display_menu')
    @patch('your_game_file.get_computer_choice', return_value='scissors')
    @patch('your_game_file.get_user_choice', side_effect=['paper', 'q'])
    @patch('your_game_file.determine_winner')
    def test_user_loses(self, mock_winner, mock_user_choice, mock_computer_choice, mock_menu):
        """
        2. Test case description: Test the game flow when the user loses (e.g., user chooses paper, computer chooses scissors).
        Expected outcome: The `determine_winner` function is called with 'paper' and 'scissors', indicating the user lost.
        """
        play_game()
        mock_winner.assert_called_with('paper', 'scissors')

    # Add more tests here to cover other scenarios like winning, tie, invalid input, etc.

if __name__ == '__main__':
    unittest.main()

