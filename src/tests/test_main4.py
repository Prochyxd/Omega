import unittest
from unittest.mock import patch
import io
import sys
import main

class TestMain(unittest.TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_choose_math_tests_interface_console_ui(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_math_tests_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to Math Tests!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['2'])
    def test_choose_math_tests_interface_gui(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_math_tests_interface()
            self.assertEqual(result, 2)
            expected_output = "Welcome to Math Tests!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['3', '1'])
    def test_choose_math_tests_interface_invalid_choice_then_valid_choice(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_math_tests_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to Math Tests!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\nInvalid choice. Please enter 1 or 2.\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['a', '1'])
    def test_choose_math_tests_interface_invalid_input_then_valid_choice(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_math_tests_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to Math Tests!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\nInvalid input. Please enter a number.\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['1'])
    def test_run_math_tests_console_ui(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            main.run_math_tests_console_ui()
            expected_output = "Running math_testsUI.math_tests()\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['2'])
    def test_run_math_tests_gui(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            main.run_math_tests_gui()
            expected_output = "Running math_testsGUI.math_tests_gui()\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['1'])
    def test_choose_ToDo_interface_console_ui(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_ToDo_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to the To-Do List Application!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['2'])
    def test_choose_ToDo_interface_gui(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_ToDo_interface()
            self.assertEqual(result, 2)
            expected_output = "Welcome to the To-Do List Application!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['3', '1'])
    def test_choose_ToDo_interface_invalid_choice_then_valid_choice(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_ToDo_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to the To-Do List Application!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\nInvalid choice. Please enter 1 or 2.\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['a', '1'])
    def test_choose_ToDo_interface_invalid_input_then_valid_choice(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_ToDo_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to the To-Do List Application!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\nInvalid input. Please enter a number.\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['1'])
    def test_run_ToDo_console_ui(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            main.run_ToDo_console_ui()
            expected_output = "Running todolistUI.todo()\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)


    @patch('builtins.input', side_effect=['1'])
    def test_choose_compression_interface_console_ui(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_compression_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to the Compression Tool!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['2'])
    def test_choose_compression_interface_gui(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_compression_interface()
            self.assertEqual(result, 2)
            expected_output = "Welcome to the Compression Tool!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['3', '1'])
    def test_choose_compression_interface_invalid_choice_then_valid_choice(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_compression_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to the Compression Tool!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\nInvalid choice. Please enter 1 or 2.\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['a', '1'])
    def test_choose_compression_interface_invalid_input_then_valid_choice(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_compression_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to the Compression Tool!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\nInvalid input. Please enter a number.\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['1'])
    def test_run_compression_console_ui(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            main.run_compression_console_ui()
            expected_output = "Running compression()\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)


    @patch('builtins.input', side_effect=['1'])
    def test_auth_choice_console_ui(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            main.auth_choice = 1
            main.run_auth_ui()
            expected_output = "Running run_auth_ui()\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()