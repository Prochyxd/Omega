import unittest
from unittest.mock import patch
import tkinter as tk
import math_testsGUI

class TestMathTestsGUI(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = math_testsGUI.MathTestsGUI(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_start_tests_with_empty_name(self):
        with patch.object(tk.messagebox, 'showerror') as mock_showerror:
            self.app.name_entry.insert(0, '')
            self.app.start_tests()
            mock_showerror.assert_called_once_with("Error", "Please enter your name.")

    def test_start_tests_with_valid_name(self):
        self.app.name_entry.insert(0, 'John')
        self.app.start_tests()
        self.assertEqual(len(self.app.category_radio_buttons), 4)
        self.assertEqual(len(self.app.difficulty_radio_buttons), 2)

    def test_start_math_tests(self):
        self.app.category_var.set("addition_subtraction")
        self.app.difficulty_var.set("easy")
        self.app.start_math_tests()
        self.assertEqual(len(self.app.problems), 10)
        self.assertEqual(self.app.current_problem_index, 0)

    def test_show_problem(self):
        problems = [
            {"problem": "2 + 2", "answer": "4"},
            {"problem": "3 * 4", "answer": "12"}
        ]
        self.app.show_problem(problems)
        self.assertEqual(self.app.current_problem_index, 0)
        self.assertEqual(self.app.problem_label['text'], "2 + 2")

    def test_check_answer_correct(self):
        self.app.category_var.set("addition_subtraction")
        self.app.difficulty_var.set("easy")
        self.app.start_math_tests()
        self.app.answer_entry.insert(0, '4')
        self.app.check_answer()
        self.assertEqual(self.app.current_problem_index, 1)
        self.assertEqual(self.app.score_var.get(), "1")

    def test_check_answer_incorrect(self):
        self.app.category_var.set("addition_subtraction")
        self.app.difficulty_var.set("easy")
        self.app.start_math_tests()
        self.app.answer_entry.insert(0, '5')
        self.app.check_answer()
        self.assertEqual(self.app.current_problem_index, 1)
        self.assertEqual(self.app.score_var.get(), "0")

    def test_end_tests(self):
        self.app.category_var.set("addition_subtraction")
        self.app.difficulty_var.set("easy")
        self.app.start_math_tests()
        self.app.end_tests()
        self.assertEqual(len(self.app.root.winfo_children()), 2)

if __name__ == '__main__':
    unittest.main()