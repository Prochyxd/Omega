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
        It then checks if the function returns the expected result and if the expected output is printed to the console.

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
        It then checks if the function returns the expected result and if the expected output
        is printed to the standard output.

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

        The test checks if the function returns the expected result and if the correct output is printed to the console.

        Mocks the built-in input function to simulate user input of '3' (invalid choice) and '1' (valid choice).
        Uses a patch to redirect the standard output to a StringIO object to capture the printed output.
        Compares the result of the function call with the expected result and the captured output with the expected output.
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

        The test mocks the built-in input function to simulate user input of 'a' and then '1'.
        It verifies that the function returns the expected result of 1.
        It also checks that the expected output is printed to the standard output.

        The expected output is:
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
    def test_run_math_tests_console_ui(self, mock_input):
        """
        Test case for the 'run_math_tests_console_ui' function in the 'main' module.

        This test case checks if the 'run_math_tests_console_ui' function correctly prints the expected output to the console.

        It uses the 'patch' decorator from the 'unittest.mock' module to mock the 'input' function and provide a predefined input value.
        It also uses the 'patch' context manager to redirect the standard output to a fake stream, allowing us to capture the printed output.

        After calling the 'run_math_tests_console_ui' function, the test case compares the captured output with the expected output using the 'assertEqual' method from the 'unittest.TestCase' class.

        If the captured output matches the expected output, the test case passes. Otherwise, it fails.

        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            main.run_math_tests_console_ui()
            expected_output = "Running math_testsUI.math_tests()\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['2'])
    def test_run_math_tests_gui(self, mock_input):
        """
        Test case for the 'run_math_tests_gui' function.

        This test case checks if the 'run_math_tests_gui' function prints the expected output to stdout.

        It patches the 'input' function to simulate user input and captures the output using 'sys.stdout'.
        The captured output is then compared to the expected output using the 'assertEqual' method.

        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            main.run_math_tests_gui()
            expected_output = "Running math_testsGUI.math_tests_gui()\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['1'])
    def test_choose_ToDo_interface_console_ui(self, mock_input):
        """
        Test case for the choose_ToDo_interface function in the main module.

        This test case checks if the function returns the expected result and if the
        output to the console matches the expected output.

        The function is patched to simulate user input of '1' when prompted to choose
        the interface. The standard output is also patched to capture the output
        printed to the console.

        The expected result is 1, indicating that the console UI was chosen. The
        expected output is a welcome message and a prompt to choose the interface.

        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_ToDo_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to the To-Do List Application!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['2'])
    def test_choose_ToDo_interface_gui(self, mock_input):
        """
        Test the choose_ToDo_interface function when the user chooses the GUI interface.
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

        The function should display a welcome message and prompt the user to choose
        the interface they want to use. If an invalid choice is entered, an error
        message should be displayed and the user should be prompted again. If a valid
        choice is entered, the function should return the chosen interface and display
        the expected output.

        This test case uses the patch decorator to mock the input function and simulate
        the user's input. It also uses the patch decorator to redirect the standard output
        to a StringIO object, allowing us to capture the printed output and compare it
        with the expected output.

        Assertions:
        - The return value of the choose_ToDo_interface function should be equal to 1.
        - The printed output should be equal to the expected output.
        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_ToDo_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to the To-Do List Application!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\nInvalid choice. Please enter 1 or 2.\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['a', '1'])
    def test_choose_ToDo_interface_invalid_input_then_valid_choice(self, mock_input):
        """
        Test case for the choose_ToDo_interface function when given an invalid input followed by a valid choice.

        The test mocks the built-in input function to simulate user input of 'a' and '1'.
        It then asserts that the return value of the choose_ToDo_interface function is equal to 1.
        Additionally, it checks that the expected output is printed to the standard output.

        Expected behavior:
        - The function should display the welcome message and prompt the user to choose an interface.
        - If the user enters an invalid input (not a number), an error message should be displayed.
        - If the user enters a valid choice (1 or 2), the function should return the chosen interface number.
        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_ToDo_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to the To-Do List Application!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\nInvalid input. Please enter a number.\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['1'])
    def test_run_ToDo_console_ui(self, mock_input):
        """
        Test case for the run_ToDo_console_ui function.

        This test case checks if the function correctly runs the ToDo console UI and produces the expected output.

        It mocks the 'input' function to simulate user input and captures the output using 'sys.stdout'.

        The expected output is compared with the actual output to ensure they match.

        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            main.run_ToDo_console_ui()
            expected_output = "Running todolistUI.todo()\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)


    @patch('builtins.input', side_effect=['1'])
    def test_choose_compression_interface_console_ui(self, mock_input):
        """
        Test the choose_compression_interface function when the user selects the console UI.

        This test case uses the patch decorator to mock the input function and simulate the user input of '1'.
        It then checks if the returned result is equal to 1, indicating that the console UI was chosen correctly.
        Additionally, it verifies that the expected output is printed to the standard output.

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

        The test patches the 'input' function to simulate user input of '3' and '1'.
        It then calls the choose_compression_interface function and asserts that the returned result is equal to 1.
        The expected output is also asserted against the value of sys.stdout to ensure the correct output is printed.

        This test case verifies the behavior of the choose_compression_interface function when an invalid choice is entered followed by a valid choice.
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

        This test case mocks the user input to simulate the scenario where the user enters an invalid input ('a') followed by a valid choice ('1').
        It verifies that the choose_compression_interface function returns the expected result (1) and prints the expected output to stdout.

        The expected output is:
        "Welcome to the Compression Tool!
        Choose the interface you want to use:
        1. Console UI
        2. GUI
        Invalid input. Please enter a number."

        This test case uses the patch decorator from the unittest.mock module to mock the built-in input function and simulate user input.
        It also uses the patch context manager to redirect the standard output (sys.stdout) to a StringIO object, allowing us to capture and assert the printed output.

        Assertions:
        - The result returned by the choose_compression_interface function is equal to 1.
        - The value printed to stdout (captured using fake_stdout.getvalue()) is equal to the expected output.
        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            result = main.choose_compression_interface()
            self.assertEqual(result, 1)
            expected_output = "Welcome to the Compression Tool!\nChoose the interface you want to use:\n1. Console UI\n2. GUI\nInvalid input. Please enter a number.\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['1'])
    def test_run_compression_console_ui(self, mock_input):
        """
        Test the run_compression_console_ui function.

        This test case checks if the output of the function matches the expected output.

        Parameters:
        - self: The test case object.
        - mock_input: The patched input function.

        Returns:
        - None
        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            main.run_compression_console_ui()
            expected_output = "Running compression()\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)


    @patch('builtins.input', side_effect=['1'])
    def test_auth_choice_console_ui(self, mock_input):
        """
        Test case for the `auth_choice_console_ui` function in the `main` module.

        This test case checks if the `run_auth_ui` function is called correctly when the user selects option 1.
        It mocks the user input to simulate the selection of option 1 and captures the output to assert against the expected output.

        Args:
            self: The test case instance.
            mock_input: The mock object for the `input` function.

        Returns:
            None
        """
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            main.auth_choice = 1
            main.run_auth_ui()
            expected_output = "Running run_auth_ui()\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()