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
        Test the choose_math_tests_interface function when the user chooses the GUI interface.
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
        It then asserts that the return value of the choose_math_tests_interface function is 1.
        It also asserts that the expected output is printed to the standard output.

        Expected output:
        "Welcome to Math Tests!
        Choose the interface you want to use:
        1. Console UI
        2. GUI
        Invalid choice. Please enter 1 or 2."
        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_math_tests_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to Math Tests!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\nInvalid choice. Please enter 1 or 2.\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['a', '1'])
    def test_choose_math_tests_interface_invalid_input_then_valid_choice(self, mock_input):
        """
        Test case for the choose_math_tests_interface function when invalid input is provided first and then a valid choice is made.

        This test case mocks the input function to simulate the user entering 'a' and then '1'. It verifies that the function returns the expected result and prints the expected output to stdout.

        Expected behavior:
        - The function should return the value 1.
        - The function should print the following message to stdout:
            "Welcome to Math Tests!
            Choose the interface you want to use:
            1. Console UI
            2. GUI
            Invalid input. Please enter a number."
        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_math_tests_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to Math Tests!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\nInvalid input. Please enter a number.\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['1'])
    def test_choose_work_with_txt_interface_console_ui(self, mock_input):
        """
        Test case for the choose_work_with_txt_interface function when choosing the console UI.

        This test case mocks the user input to simulate choosing option 1 (console UI).
        It verifies that the function returns the expected result and prints the expected output to stdout.
        """

        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_work_with_txt_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to the program!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['2'])
    def test_choose_work_with_txt_interface_gui(self, mock_input):
        """
        Test the choose_work_with_txt_interface function when the user chooses the GUI interface.
        
        This test case mocks the user input to simulate the user choosing the GUI interface (input value of '2').
        It then captures the output of the function and asserts that the returned result is equal to 2.
        Additionally, it checks that the expected output message is printed to the standard output.
        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_work_with_txt_interface()
            self.assertEqual(result, 2)
            expected_output = "Welcome to the program!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['3', '1'])
    def test_choose_work_with_txt_interface_invalid_choice_then_valid_choice(self, mock_input):
        """
        Test case for the choose_work_with_txt_interface function when an invalid choice is entered first and then a valid choice is entered.

        The test patches the 'input' function to simulate user input of '3' followed by '1'.
        It then checks the return value of the choose_work_with_txt_interface function and asserts that it is equal to 1.
        It also checks the output printed to the console and asserts that it matches the expected output.

        Expected behavior:
        - The program should print the welcome message and prompt the user to choose an interface.
        - Since an invalid choice of '3' is entered, the program should print an error message asking for a valid choice.
        - Finally, the program should accept the valid choice of '1' and return 1.

        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_work_with_txt_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to the program!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\nInvalid choice. Please enter 1 or 2.\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['a', '1'])
    def test_choose_work_with_txt_interface_invalid_input_then_valid_choice(self, mock_input):
        """
        Test case for the choose_work_with_txt_interface function when invalid input is followed by a valid choice.

        This test case mocks the user input to simulate the scenario where the user enters 'a' as the first input, which is invalid,
        and then enters '1' as the second input, which is a valid choice. The test verifies that the function returns the expected result
        and that the correct output is printed to the console.

        Args:
            self: The test case object.
            mock_input: The mock object for the built-in input function.

        Returns:
            None
        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_work_with_txt_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to the program!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\nInvalid input. Please enter a number.\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()