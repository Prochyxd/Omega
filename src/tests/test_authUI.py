import unittest
from unittest.mock import patch
import io
import sys
from authUI import AuthenticationUI

class TestAuthenticationUI(unittest.TestCase):
    @patch('authUI.Login.login')
    def test_login(self, mock_login):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            # Simulate user input
            with patch('builtins.input', side_effect=['1']):
                auth_ui = AuthenticationUI()
                auth_ui.show_menu()

            # Check if the login function was called
            mock_login.assert_called_once()

    @patch('authUI.Registration.register')
    def test_register(self, mock_register):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            # Simulate user input
            with patch('builtins.input', side_effect=['2']):
                auth_ui = AuthenticationUI()
                auth_ui.show_menu()

            # Check if the register function was called
            mock_register.assert_called_once()

    def test_exit(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            # Simulate user input
            with patch('builtins.input', side_effect=['3']):
                auth_ui = AuthenticationUI()
                auth_ui.show_menu()

            # Check if the correct output was printed
            expected_output = "Goodbye!\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_invalid_choice(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            # Simulate user input
            with patch('builtins.input', side_effect=['4', '3']):
                auth_ui = AuthenticationUI()
                auth_ui.show_menu()

            # Check if the correct output was printed
            expected_output = "Invalid choice. Please choose again.\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()