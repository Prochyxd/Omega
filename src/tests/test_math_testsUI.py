import unittest
from unittest.mock import patch
import io
import sys
import math_testsUI

class TestMathTestsUI(unittest.TestCase):
    @patch('math_testsUI.math_tests_module.load_problems')
    @patch('math_testsUI.math_tests_module.choose_problems')
    @patch('math_testsUI.math_tests_module.choose_difficulty')
    @patch('math_testsUI.math_tests_module.get_problem')
    @patch('math_testsUI.math_tests_module.get_score')
    @patch('math_testsUI.math_tests_module.save_score')
    @patch('math_testsUI.open')
    def test_math_tests(self, mock_open, mock_save_score, mock_get_score, mock_get_problem, mock_choose_difficulty, mock_choose_problems, mock_load_problems):
        mock_open.return_value.__enter__.return_value = io.StringIO()
        mock_load_problems.return_value = ['problem1', 'problem2', 'problem3']
        mock_choose_problems.return_value = 'category1'
        mock_choose_difficulty.return_value = 'difficulty1'
        mock_get_problem.side_effect = ['problem1', 'problem2', 'problem3']
        mock_get_score.return_value = 30
        math_testsUI.math_tests()
        mock_open.assert_called_once_with("files/math_problems_leaderboard.json", "r", encoding="utf-8")
        mock_save_score.assert_called_once_with('mock_name', 30, mock_get_score.return_value)
        self.assertEqual(mock_open.return_value.__enter__.return_value.getvalue(), "1. mock_name - 30 - 0.00 seconds\n")

    @patch('math_testsUI.math_tests_module.load_problems')
    @patch('math_testsUI.math_tests_module.choose_problems')
    @patch('math_testsUI.math_tests_module.choose_difficulty')
    @patch('math_testsUI.math_tests_module.get_problem')
    @patch('math_testsUI.math_tests_module.get_score')
    @patch('math_testsUI.math_tests_module.save_score')
    @patch('math_testsUI.open')
    def test_math_tests_leaderboard_file_not_found(self, mock_open, mock_save_score, mock_get_score, mock_get_problem, mock_choose_difficulty, mock_choose_problems, mock_load_problems):
        mock_open.side_effect = FileNotFoundError
        mock_load_problems.return_value = ['problem1', 'problem2', 'problem3']
        mock_choose_problems.return_value = 'category1'
        mock_choose_difficulty.return_value = 'difficulty1'
        mock_get_problem.side_effect = ['problem1', 'problem2', 'problem3']
        mock_get_score.return_value = 30
        math_testsUI.math_tests()
        mock_open.assert_called_once_with("files/math_problems_leaderboard.json", "r", encoding="utf-8")
        mock_save_score.assert_called_once_with('mock_name', 30, mock_get_score.return_value)
        self.assertEqual(mock_open.return_value.__enter__.return_value.getvalue(), "Leaderboard file not found.\n")

    @patch('math_testsUI.math_tests_module.load_problems')
    @patch('math_testsUI.math_tests_module.choose_problems')
    @patch('math_testsUI.math_tests_module.choose_difficulty')
    @patch('math_testsUI.math_tests_module.get_problem')
    @patch('math_testsUI.math_tests_module.get_score')
    @patch('math_testsUI.math_tests_module.save_score')
    @patch('math_testsUI.open')
    def test_math_tests_no_problems(self, mock_open, mock_save_score, mock_get_score, mock_get_problem, mock_choose_difficulty, mock_choose_problems, mock_load_problems):
        mock_open.return_value.__enter__.return_value = io.StringIO()
        mock_load_problems.return_value = []
        math_testsUI.math_tests()
        mock_open.assert_called_once_with("files/math_problems_leaderboard.json", "r", encoding="utf-8")
        self.assertEqual(mock_open.return_value.__enter__.return_value.getvalue(), "No problems found.\n")

if __name__ == '__main__':
    unittest.main()