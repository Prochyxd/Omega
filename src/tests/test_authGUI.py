import unittest
from unittest.mock import patch
import tkinter as tk
from tkinter import messagebox
import json
import hashlib
import re
import os
from authGUI import AuthGUI, RegisterGUI

class TestAuthGUI(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = AuthGUI(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_login_successful(self):
        # Simulate user input
        self.app.username_entry.insert(0, "testuser")
        self.app.password_entry.insert(0, "password123")

        # Create a mock json file with user data
        json_data = {
            "testuser": {
                "password": hashlib.sha256("password123".encode()).hexdigest()
            }
        }
        with open("files/login.json", "w") as f:
            json.dump(json_data, f)

        # Patch the messagebox.showinfo method to check if it was called with the correct arguments
        with patch.object(messagebox, "showinfo") as mock_showinfo:
            self.app.login()

            # Check if the messagebox.showinfo method was called with the correct arguments
            mock_showinfo.assert_called_once_with("Success", "Login successful.")

    def test_login_invalid_username(self):
        # Simulate user input
        self.app.username_entry.insert(0, "invaliduser")
        self.app.password_entry.insert(0, "password123")

        # Create a mock json file with user data
        json_data = {
            "testuser": {
                "password": hashlib.sha256("password123".encode()).hexdigest()
            }
        }
        with open("files/login.json", "w") as f:
            json.dump(json_data, f)

        # Patch the messagebox.showerror method to check if it was called with the correct arguments
        with patch.object(messagebox, "showerror") as mock_showerror:
            self.app.login()

            # Check if the messagebox.showerror method was called with the correct arguments
            mock_showerror.assert_called_once_with("Error", "Username not found. Please enter a valid username.")

    def test_login_incorrect_password(self):
        # Simulate user input
        self.app.username_entry.insert(0, "testuser")
        self.app.password_entry.insert(0, "incorrectpassword")

        # Create a mock json file with user data
        json_data = {
            "testuser": {
                "password": hashlib.sha256("password123".encode()).hexdigest()
            }
        }
        with open("files/login.json", "w") as f:
            json.dump(json_data, f)

        # Patch the messagebox.showerror method to check if it was called with the correct arguments
        with patch.object(messagebox, "showerror") as mock_showerror:
            self.app.login()

            # Check if the messagebox.showerror method was called with the correct arguments
            mock_showerror.assert_called_once_with("Error", "Incorrect password. Please enter a valid password.")

class TestRegisterGUI(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = RegisterGUI(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_register_successful(self):
        # Simulate user input
        self.app.username_entry.insert(0, "newuser")
        self.app.password_entry.insert(0, "password123")
        self.app.password2_entry.insert(0, "password123")
        self.app.email_entry.insert(0, "test@example.com")

        # Create a mock json file with user data
        json_data = {
            "testuser": {
                "password": hashlib.sha256("password123".encode()).hexdigest(),
                "email": "test@example.com"
            }
        }
        with open("files/login.json", "w") as f:
            json.dump(json_data, f)

        # Patch the messagebox.showinfo method to check if it was called with the correct arguments
        with patch.object(messagebox, "showinfo") as mock_showinfo:
            self.app.register()

            # Check if the messagebox.showinfo method was called with the correct arguments
            mock_showinfo.assert_called_once_with("Success", "Registration successful.")

    def test_register_invalid_username(self):
        # Simulate user input
        self.app.username_entry.insert(0, "inv")
        self.app.password_entry.insert(0, "password123")
        self.app.password2_entry.insert(0, "password123")
        self.app.email_entry.insert(0, "test@example.com")

        # Patch the messagebox.showerror method to check if it was called with the correct arguments
        with patch.object(messagebox, "showerror") as mock_showerror:
            self.app.register()

            # Check if the messagebox.showerror method was called with the correct arguments
            mock_showerror.assert_called_once_with("Error", "Invalid username. Please enter a username that is between 3 and 20 characters long and only contains letters, numbers, and underscores.")

    def test_register_invalid_password(self):
        # Simulate user input
        self.app.username_entry.insert(0, "newuser")
        self.app.password_entry.insert(0, "password")
        self.app.password2_entry.insert(0, "password")
        self.app.email_entry.insert(0, "test@example.com")

        # Patch the messagebox.showerror method to check if it was called with the correct arguments
        with patch.object(messagebox, "showerror") as mock_showerror:
            self.app.register()

            # Check if the messagebox.showerror method was called with the correct arguments
            mock_showerror.assert_called_once_with("Error", "Invalid password. Please enter a password that is at least 8 characters long and contains at least one letter and one number.")

    def test_register_passwords_do_not_match(self):
        # Simulate user input
        self.app.username_entry.insert(0, "newuser")
        self.app.password_entry.insert(0, "password123")
        self.app.password2_entry.insert(0, "password456")
        self.app.email_entry.insert(0, "test@example.com")

        # Patch the messagebox.showerror method to check if it was called with the correct arguments
        with patch.object(messagebox, "showerror") as mock_showerror:
            self.app.register()

            # Check if the messagebox.showerror method was called with the correct arguments
            mock_showerror.assert_called_once_with("Error", "Passwords do not match. Please re-enter your password.")

    def test_register_invalid_email(self):
        # Simulate user input
        self.app.username_entry.insert(0, "newuser")
        self.app.password_entry.insert(0, "password123")
        self.app.password2_entry.insert(0, "password123")
        self.app.email_entry.insert(0, "invalidemail")

        # Patch the messagebox.showerror method to check if it was called with the correct arguments
        with patch.object(messagebox, "showerror") as mock_showerror:
            self.app.register()

            # Check if the messagebox.showerror method was called with the correct arguments
            mock_showerror.assert_called_once_with("Error", "Invalid email address. Please enter a valid email address.")

if __name__ == '__main__':
    unittest.main()