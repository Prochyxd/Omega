
    
import unittest
from unittest.mock import patch
import io
import sys
import main

class TestMain(unittest.TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_choose_math_tests_interface_console_ui(self, mock_input):
        """
        Test case for the choose_math_tests_interface function when using the console UI.

        This test case checks if the function returns the correct value and prints the expected output to the console.

        Args:
            self: The test case instance.
            mock_input: The patched input function.

        Returns:
            None
        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_math_tests_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to Math Tests!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['2'])
    def test_choose_math_tests_interface_gui(self, mock_input):
        """
        Test the choose_math_tests_interface function when GUI interface is chosen.

        This test case mocks the user input to simulate the selection of the GUI interface.
        It then checks if the function returns the expected result and if the expected output
        is printed to the standard output.

        Args:
            self: The test case object.
            mock_input: The mock object for the built-in input function.

        Returns:
            None
        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_math_tests_interface()
            self.assertEqual(result, 2)
            expected_output = "Welcome to Math Tests!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['3', '1'])
    def test_choose_math_tests_interface_invalid_choice_then_valid_choice(self, mock_input):
        """
        Test case for the choose_math_tests_interface function when an invalid choice is entered first and then a valid choice is entered.

        This test case checks if the function correctly handles an invalid choice by displaying an error message and prompting the user to enter a valid choice.

        It also checks if the function returns the correct value and if the expected output is printed to the console.

        The patch decorator is used to mock the input function and simulate the user's input.

        Parameters:
        - self: The test case instance.
        - mock_input: The mocked input function.

        Returns:
        - None
        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_math_tests_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to Math Tests!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\nInvalid choice. Please enter 1 or 2.\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['a', '1'])
    def test_choose_math_tests_interface_invalid_input_then_valid_choice(self, mock_input):
        """
        Test case for the choose_math_tests_interface function when invalid input is followed by a valid choice.

        This test case checks if the function correctly handles invalid input followed by a valid choice. It mocks the input
        function to simulate the user entering 'a' and then '1'. The function is expected to display a welcome message and
        prompt the user to choose an interface. Since the first input is invalid, the function should display an error
        message and ask for a valid input. After the user enters '1', the function should return the chosen interface and
        display the expected output.

        The expected output is:
        - A welcome message
        - A prompt to choose an interface
        - An error message for invalid input
        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_math_tests_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to Math Tests!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\nInvalid input. Please enter a number.\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['1'])
    def test_choose_ToDo_interface_console_ui(self, mock_input):
        """
        Test the choose_ToDo_interface function when the user selects the console UI.

        This test case mocks the user input to simulate the selection of the console UI.
        It verifies that the function returns the expected result and prints the expected output.

        Args:
            self: The test case object.
            mock_input: The mock object for the input function.

        Returns:
            None
        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_ToDo_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to the To-Do List Application!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['2'])
    def test_choose_ToDo_interface_gui(self, mock_input):
        """
        Test the choose_ToDo_interface function when GUI interface is chosen.

        This test case mocks the user input to simulate the selection of GUI interface.
        It then checks if the returned result is equal to 2, indicating that GUI interface was chosen.
        It also checks if the expected output is printed to the standard output.
        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_ToDo_interface()
            self.assertEqual(result, 2)
            expected_output = "Welcome to the To-Do List Application!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['3', '1'])
    def test_choose_ToDo_interface_invalid_choice_then_valid_choice(self, mock_input):
        """
        Test case for the choose_ToDo_interface function when an invalid choice is entered first and then a valid choice is entered.

        The test mocks the input function to simulate user input of '3' (invalid choice) and then '1' (valid choice).
        It checks if the function returns the expected result and if the output printed to stdout matches the expected output.
        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_ToDo_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to the To-Do List Application!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\nInvalid choice. Please enter 1 or 2.\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['a', '1'])
    def test_choose_ToDo_interface_invalid_input_then_valid_choice(self, mock_input):
        """
        Test case for the choose_ToDo_interface function when invalid input is followed by a valid choice.

        This test case mocks the built-in input function to simulate user input of 'a' followed by '1'.
        It verifies that the choose_ToDo_interface function returns the expected result and prints the expected output.

        The expected output is:
        "Welcome to the To-Do List Application!
        Choose the interface you want to use:
        1. Console UI
        2. GUI
        Invalid input. Please enter a number.\n"

        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_ToDo_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to the To-Do List Application!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\nInvalid input. Please enter a number.\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()