import unittest
from unittest.mock import patch
import io
import sys
from math_tests import choose_difficulty

class TestMathTests(unittest.TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_choose_difficulty_easy(self, mock_input):
        expected_output = "Choose a difficulty:\n1. Easy\n2. Hard\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = choose_difficulty({"easy": "easy_problems", "hard": "hard_problems"})
            self.assertEqual(fake_stdout.getvalue(), expected_output)
            self.assertEqual(result, "easy_problems")

    @patch('builtins.input', side_effect=['2'])
    def test_choose_difficulty_hard(self, mock_input):
        expected_output = "Choose a difficulty:\n1. Easy\n2. Hard\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = choose_difficulty({"easy": "easy_problems", "hard": "hard_problems"})
            self.assertEqual(fake_stdout.getvalue(), expected_output)
            self.assertEqual(result, "hard_problems")

    @patch('builtins.input', side_effect=['3', '2'])
    def test_choose_difficulty_invalid_choice_then_hard(self, mock_input):
        expected_output = "Choose a difficulty:\n1. Easy\n2. Hard\nInvalid choice. Please try again.\nChoose a difficulty:\n1. Easy\n2. Hard\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = choose_difficulty({"easy": "easy_problems", "hard": "hard_problems"})
            self.assertEqual(fake_stdout.getvalue(), expected_output)
            self.assertEqual(result, "hard_problems")

    @patch('builtins.input', side_effect=['a', '2'])
    def test_choose_difficulty_invalid_input_then_hard(self, mock_input):
        expected_output = "Choose a difficulty:\n1. Easy\n2. Hard\nInvalid input. Please enter a number.\nChoose a difficulty:\n1. Easy\n2. Hard\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = choose_difficulty({"easy": "easy_problems", "hard": "hard_problems"})
            self.assertEqual(fake_stdout.getvalue(), expected_output)
            self.assertEqual(result, "hard_problems")

if __name__ == '__main__':
    unittest.main()