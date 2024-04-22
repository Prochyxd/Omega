import unittest
from unittest.mock import patch
import io
import sys
import main

class TestMain(unittest.TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_choose_math_tests_interface_console_ui(self, mock_input):
        """
        Test the choose_math_tests_interface function when the user selects the console UI.
        
        This test case mocks the user input to simulate the selection of the console UI.
        It verifies that the function returns the expected result and prints the expected output to stdout.
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

        This test case mocks the user input to simulate the selection of GUI interface.
        It then checks if the returned result is equal to 2, indicating that GUI interface was chosen.
        It also checks if the expected output is printed to the standard output.
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

        The test mocks the input function to simulate the user entering '3' and '1' as choices.
        It checks that the function returns the expected result and that the output printed to stdout matches the expected output.
        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_math_tests_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to Math Tests!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\nInvalid choice. Please enter 1 or 2.\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['a', '1'])
    def test_choose_math_tests_interface_invalid_input_then_valid_choice(self, mock_input):
        """
        Test case to verify the behavior of the choose_math_tests_interface function
        when an invalid input is provided followed by a valid choice.

        The function is expected to display a welcome message and prompt the user
        to choose an interface. If an invalid input is provided, it should display
        an error message and ask for a valid input. Once a valid choice is made,
        the function should return the chosen interface number and display the
        expected output.

        This test case uses the patch decorator to mock the built-in input function
        and simulate the user's input.

        Args:
            self: The test case instance.
            mock_input: The mocked input function.

        Returns:
            None
        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_math_tests_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to Math Tests!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\nInvalid input. Please enter a number.\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()

