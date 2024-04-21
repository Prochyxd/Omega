import json
import hashlib
import re
import os

class Registration():
    """
    Class representing the registration process for a user.

    Attributes:
    - username (str): The username entered by the user.
    - password (str): The password entered by the user.
    - password2 (str): The password entered by the user for confirmation.
    - email (str): The email address entered by the user.
    - username_pattern (Pattern): The regular expression pattern for validating the username.
    - password_pattern (Pattern): The regular expression pattern for validating the password.
    - email_pattern (Pattern): The regular expression pattern for validating the email address.

    Methods:
    - register(): Performs the registration process by prompting the user for input and validating the input.
    """

    def __init__(self):
        self.username = ""
        self.password = ""
        self.password2 = ""
        self.email = ""
        self.username_pattern = re.compile("^[a-zA-Z0-9_]{3,20}$")
        self.password_pattern = re.compile("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")
        self.email_pattern = re.compile("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    
    def register(self):
        """
        Performs the registration process by prompting the user for input and validating the input.

        The user is prompted to enter their username, password, password confirmation, and email address.
        The input is validated against the predefined regular expression patterns.
        If the input is valid, the user's information is stored in a JSON file.
        If the username already exists in the JSON file, the registration process is aborted.

        Returns:
        - None
        """
        while True:
            self.username = input("Enter your username: ")
            if self.username_pattern.match(self.username):
                break
            else:
                print("Invalid username. Please enter a username that is between 3 and 20 characters long and only contains letters, numbers, and underscores.")
        
        while True:
            self.password = input("Enter your password: ")
            if self.password_pattern.match(self.password):
                break
            else:
                print("Invalid password. Please enter a password that is at least 8 characters long and contains at least one letter and one number.")
        
        while True:
            self.password2 = input("Re-enter your password: ")
            if self.password == self.password2:
                break
            else:
                print("Passwords do not match. Please re-enter your password.")
        
        while True:
            self.email = input("Enter your email address: ")
            if self.email_pattern.match(self.email):
                break
            else:
                print("Invalid email address. Please enter a valid email address.")
        
        if not os.path.exists("files\login.json"):
            with open("files\login.json", "w") as f:
                f.write("{}")

        with open("files\login.json", "r") as f:
            data = json.load(f)
        
        if self.username in data:
            print("Username already exists. Please choose a different username.")
            return
        
        data[self.username] = {"password": hashlib.sha256(self.password.encode()).hexdigest(), "email": self.email}
        
        with open("files\login.json", "w") as f:
            json.dump(data, f)
        
        print("Registration successful.")

class Login():
    """
    Represents a login process for a user.

    Attributes:
        username (str): The username entered by the user.
        password (str): The password entered by the user.
    """

    def __init__(self):
        self.username = ""
        self.password = ""
    
    def login(self):
        """
        Performs the login process.

        This method prompts the user to enter their username and password.
        It then checks if the username exists in the login data stored in "files\login.json".
        If the username is found and the password matches, it prints "Login successful" and exits the loop.
        If the username is not found or the password is incorrect, it prints an appropriate error message and continues the loop.
        """
        while True:
            self.username = input("Enter your username: ")
            self.password = input("Enter your password: ")
            
            with open("files\login.json", "r") as f:
                data = json.load(f)
            
            if self.username not in data:
                print("Username not found. Please enter a valid username.")
                continue
            
            if data[self.username]["password"] == hashlib.sha256(self.password.encode()).hexdigest():
                print("Login successful.")
                break
            else:
                print("Incorrect password. Please enter a valid password.")
