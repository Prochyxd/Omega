
import unittest
from unittest.mock import patch
import io
import sys
import main

class TestMain(unittest.TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_choose_math_tests_interface_console_ui(self, mock_input):
        """
        Test the choose_math_tests_interface function when the user chooses the console UI.

        This test case mocks the user input to simulate the user choosing option 1 (console UI).
        It then checks if the function returns the expected result (1) and if the expected output
        is printed to the standard output.

        Args:
            self: The test case object.
            mock_input: The mock object for the input function.

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

        This test case mocks the user input to simulate the selection of GUI interface.
        It then captures the output printed to stdout and asserts that the result is equal to 2.
        Finally, it checks if the expected output matches the captured output.

        Args:
            self: The test case object.
            mock_input: The mock object for the input function.

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

        The test mocks the input function to simulate the user entering '3' and '1' as choices.
        It checks that the function returns the expected result (1) and that the correct output is printed to stdout.

        Expected behavior:
        - The function should display the welcome message and prompt the user to choose an interface.
        - If an invalid choice is entered (not 1 or 2), the function should display an error message and prompt again.
        - If a valid choice is entered (1 or 2), the function should return the chosen interface and print the expected output.

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

        This test case checks if the function correctly handles invalid input by displaying an error message and prompting the user to enter a number. It also verifies that the function returns the correct choice and prints the expected output to the console.

        Args:
            self: The test case object.
            mock_input: The patched input function that provides the input values for the test.

        Returns:
            None
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
        Finally, it verifies that the expected output is printed to the standard output.
        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_ToDo_interface()
            self.assertEqual(result, 2)
            expected_output = "Welcome to the To-Do List Application!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['3', '1'])
    def test_choose_ToDo_interface_invalid_choice_then_valid_choice(self, mock_input):
        """
        Test case to verify the behavior of the choose_ToDo_interface function
        when an invalid choice is entered followed by a valid choice.

        The function is expected to display a welcome message and prompt the user
        to choose the interface they want to use. If an invalid choice is entered,
        an error message should be displayed. If a valid choice is entered, the
        function should return the chosen interface and display the expected output.

        The patch decorator is used to mock the input function and provide a sequence
        of values to simulate the user's input during the test.

        Assertions:
        - The result of the function should be equal to 1 (indicating the chosen interface).
        - The output printed to stdout should be equal to the expected output.
        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_ToDo_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to the To-Do List Application!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\nInvalid choice. Please enter 1 or 2.\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['a', '1'])
    def test_choose_ToDo_interface_invalid_input_then_valid_choice(self, mock_input):
        """
        Test case for the choose_ToDo_interface function when invalid input is given first and then a valid choice is made.

        This test case mocks the input function to simulate the user entering 'a' and then '1'.
        It verifies that the choose_ToDo_interface function returns the expected result and prints the expected output to stdout.

        Expected behavior:
        - The function should prompt the user to choose the interface.
        - If the user enters an invalid input (not a number), it should display an error message and prompt again.
        - If the user enters a valid choice (1 or 2), it should return the chosen interface number and print a welcome message.

        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_ToDo_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to the To-Do List Application!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\nInvalid input. Please enter a number.\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)


    @patch('builtins.input', side_effect=['1'])
    def test_choose_compression_interface_console_ui(self, mock_input):
        """
        Test the choose_compression_interface function when the user selects the console UI.

        This test case mocks the user input to simulate the selection of the console UI.
        It verifies that the function returns the expected result and prints the expected output.

        Args:
            self: The test case object.
            mock_input: The mock object for the input function.

        Returns:
            None
        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_compression_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to the Compression Tool!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['2'])
    def test_choose_compression_interface_gui(self, mock_input):
        """
        Test the choose_compression_interface function when the user chooses the GUI interface.
        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_compression_interface()
            self.assertEqual(result, 2)
            expected_output = "Welcome to the Compression Tool!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['3', '1'])
    def test_choose_compression_interface_invalid_choice_then_valid_choice(self, mock_input):
        """
        Test case for the choose_compression_interface function when an invalid choice is entered first and then a valid choice is entered.

        The test mocks the input function to simulate user input of '3' (invalid choice) and then '1' (valid choice).
        It checks if the function returns the expected result and if the expected output is printed to stdout.

        Expected behavior:
        - The function should return the valid choice (1).
        - The expected output should be "Welcome to the Compression Tool!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\nInvalid choice. Please enter 1 or 2.\n"
        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_compression_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to the Compression Tool!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\nInvalid choice. Please enter 1 or 2.\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['a', '1'])
    def test_choose_compression_interface_invalid_input_then_valid_choice(self, mock_input):
        """
        Test case for the choose_compression_interface function when invalid input is given first and then a valid choice is made.

        The test mocks the input function to simulate the user entering 'a' and then '1'.
        It asserts that the return value of the choose_compression_interface function is 1.
        It also asserts that the expected output is printed to the standard output.

        The expected output is:
        "Welcome to the Compression Tool!
        Choose the interface you want to use:
        1. Console UI
        2. GUI
        Invalid input. Please enter a number.
        "

        This test ensures that the function handles invalid input correctly and provides the expected output.
        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_compression_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to the Compression Tool!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\nInvalid input. Please enter a number.\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()