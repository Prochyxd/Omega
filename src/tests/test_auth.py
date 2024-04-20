import unittest
from unittest.mock import patch
import io
import sys
import os
import json
import hashlib
import re
from auth import Registration

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.registration = Registration()

    @patch('builtins.input', side_effect=['username123', 'password123', 'password123', 'test@example.com'])
    def test_valid_registration(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            with patch('builtins.open', create=True) as mock_open:
                mock_open.return_value.__enter__.return_value = io.StringIO()
                self.registration.register()

                # Check if the correct output was printed
                expected_output = "Registration successful.\n"
                self.assertEqual(fake_stdout.getvalue(), expected_output)

                # Check if the login.json file was created and updated correctly
                mock_open.assert_called_with("files\login.json", "w")
                mock_open.return_value.__enter__.return_value.write.assert_called_with("{}")
                mock_open.return_value.__enter__.return_value.seek.assert_called_with(0)
                mock_open.return_value.__enter__.return_value.truncate.assert_called_with(0)
                mock_open.assert_called_with("files\login.json", "r")
                json_data = json.load(mock_open.return_value.__enter__.return_value)
                self.assertEqual(json_data, {"username123": {"password": hashlib.sha256('password123'.encode()).hexdigest(), "email": "test@example.com"}})

    @patch('builtins.input', side_effect=['username', 'password', 'password', 'test@example.com'])
    def test_invalid_username(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            with patch('builtins.open', create=True) as mock_open:
                mock_open.return_value.__enter__.return_value = io.StringIO()
                self.registration.register()

                # Check if the correct output was printed
                expected_output = "Invalid username. Please enter a username that is between 3 and 20 characters long and only contains letters, numbers, and underscores.\n"
                self.assertEqual(fake_stdout.getvalue(), expected_output)

                # Check if the login.json file was not created or updated
                mock_open.assert_not_called()

    @patch('builtins.input', side_effect=['username123', 'password', 'password', 'test@example.com'])
    def test_invalid_password(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            with patch('builtins.open', create=True) as mock_open:
                mock_open.return_value.__enter__.return_value = io.StringIO()
                self.registration.register()

                # Check if the correct output was printed
                expected_output = "Invalid password. Please enter a password that is at least 8 characters long and contains at least one letter and one number.\n"
                self.assertEqual(fake_stdout.getvalue(), expected_output)

                # Check if the login.json file was not created or updated
                mock_open.assert_not_called()

    @patch('builtins.input', side_effect=['username123', 'password123', 'password456', 'test@example.com'])
    def test_password_mismatch(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            with patch('builtins.open', create=True) as mock_open:
                mock_open.return_value.__enter__.return_value = io.StringIO()
                self.registration.register()

                # Check if the correct output was printed
                expected_output = "Passwords do not match. Please re-enter your password.\n"
                self.assertEqual(fake_stdout.getvalue(), expected_output)

                # Check if the login.json file was not created or updated
                mock_open.assert_not_called()

    @patch('builtins.input', side_effect=['username123', 'password123', 'password123', 'invalid_email'])
    def test_invalid_email(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            with patch('builtins.open', create=True) as mock_open:
                mock_open.return_value.__enter__.return_value = io.StringIO()
                self.registration.register()

                # Check if the correct output was printed
                expected_output = "Invalid email address. Please enter a valid email address.\n"
                self.assertEqual(fake_stdout.getvalue(), expected_output)

                # Check if the login.json file was not created or updated
                mock_open.assert_not_called()

    @patch('builtins.input', side_effect=['username123', 'password123', 'password123', 'test@example.com'])
    def test_existing_username(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            with patch('builtins.open', create=True) as mock_open:
                mock_open.return_value.__enter__.return_value = io.StringIO(json.dumps({"username123": {"password": "hashed_password", "email": "existing@example.com"}}))
                self.registration.register()

                # Check if the correct output was printed
                expected_output = "Username already exists. Please choose a different username.\n"
                self.assertEqual(fake_stdout.getvalue(), expected_output)

                # Check if the login.json file was not updated
                mock_open.assert_called_with("files\login.json", "r")
                mock_open.assert_not_called()

from auth import Login

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.login = Login()

    @patch('builtins.input', side_effect=['username123', 'password123'])
    def test_valid_login(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            with patch('builtins.open', create=True) as mock_open:
                mock_open.return_value.__enter__.return_value = io.StringIO(json.dumps({"username123": {"password": hashlib.sha256('password123'.encode()).hexdigest()}}))
                self.login.login()

                # Check if the correct output was printed
                expected_output = "Login successful.\n"
                self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['nonexistent_user', 'password123'])
    def test_invalid_username(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            with patch('builtins.open', create=True) as mock_open:
                mock_open.return_value.__enter__.return_value = io.StringIO(json.dumps({"username123": {"password": hashlib.sha256('password123'.encode()).hexdigest()}}))
                self.login.login()

                # Check if the correct output was printed
                expected_output = "Username not found. Please enter a valid username.\n"
                self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['username123', 'incorrect_password'])
    def test_invalid_password(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            with patch('builtins.open', create=True) as mock_open:
                mock_open.return_value.__enter__.return_value = io.StringIO(json.dumps({"username123": {"password": hashlib.sha256('password123'.encode()).hexdigest()}}))
                self.login.login()

                # Check if the correct output was printed
                expected_output = "Incorrect password. Please enter a valid password.\n"
                self.assertEqual(fake_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()