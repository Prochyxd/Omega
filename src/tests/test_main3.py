
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
        It then checks if the function returns the expected result and if the expected output is printed to stdout.

        Args:
            self: The test case object.
            mock_input: The mock object for the built-in input function.

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
        Test the 'choose_math_tests_interface' function when GUI interface is chosen.

        This test case mocks the user input to simulate the selection of GUI interface.
        It then checks if the function returns the expected result and if the expected output
        is printed to the standard output.

        Args:
            self: The test case object.
            mock_input: The mock object for the 'input' function.

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
        It checks if the function returns the expected result and if the output printed to stdout matches the expected output.
        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_math_tests_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to Math Tests!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\nInvalid choice. Please enter 1 or 2.\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['a', '1'])
    def test_choose_math_tests_interface_invalid_input_then_valid_choice(self, mock_input):
        """
        Test case for the choose_math_tests_interface function when invalid input is given first and then a valid choice is made.

        This test case mocks the input function to simulate the user entering 'a' and then '1'. It verifies that the choose_math_tests_interface function returns the expected result and prints the expected output to stdout.

        The expected output is:
        "Welcome to Math Tests!
        Choose the interface you want to use:
        1. Console UI
        2. GUI
        Invalid input. Please enter a number.
        "

        The test asserts that the result is equal to 1 and the printed output matches the expected output.
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
            mock_input: The mock object for the built-in input function.

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
        Test case for the choose_ToDo_interface function when GUI interface is chosen.

        This test case mocks the user input to simulate the selection of GUI interface.
        It verifies that the function returns the expected result and prints the expected output.

        Args:
            self: The test case object.
            mock_input: The mocked input function.

        Returns:
            None
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
        an error message should be displayed and the user should be prompted again
        to enter a valid choice. Once a valid choice is entered, the function should
        return the chosen interface and display the expected output.

        This test case uses the patch decorator to mock the input function and simulate
        the user's input. It also uses the patch decorator to redirect the standard output
        to a StringIO object, allowing us to capture and compare the printed output.

        The expected output is defined in the 'expected_output' variable and compared
        against the actual output captured from the fake standard output.

        The result of the choose_ToDo_interface function is also compared against the
        expected result to ensure the correct interface is returned.

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

        This test case checks if the function returns the correct result and prints the expected output to stdout.

        Parameters:
        - self: The test case instance.
        - mock_input: The patched input function.

        Returns:
        - None
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
        This test case uses the patch decorator to mock the built-in input function and simulate the user input of '1'.
        It then checks if the return value of the choose_compression_interface function is equal to 1.
        Additionally, it verifies that the expected output is printed to the standard output.
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
        Test the choose_compression_interface function when GUI interface is chosen.

        This test case mocks the user input to simulate the selection of GUI interface.
        It then checks if the returned result matches the expected value.
        It also checks if the output printed to stdout matches the expected output.
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

        The test mocks the input function to simulate the user entering '3' and then '1'. It verifies that the function returns the expected result and that the correct output is printed to stdout.

        Expected behavior:
        - The function should return the valid choice entered by the user.
        - The output printed to stdout should match the expected output.

        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_compression_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to the Compression Tool!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\nInvalid choice. Please enter 1 or 2.\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['a', '1'])
    def test_choose_compression_interface_invalid_input_then_valid_choice(self, mock_input):
        """
        Test case for the choose_compression_interface function when invalid input is followed by a valid choice.

        This test case mocks the input function to simulate the user entering 'a' and then '1'.
        It verifies that the choose_compression_interface function returns the expected result and prints the expected output.

        The expected output is:
        "Welcome to the Compression Tool!
        Choose the interface you want to use:
        1. Console UI
        2. GUI
        Invalid input. Please enter a number."

        The test asserts that the result returned by the choose_compression_interface function is equal to 1.
        It also asserts that the output printed to stdout matches the expected output.
        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_compression_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to the Compression Tool!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\nInvalid input. Please enter a number.\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()