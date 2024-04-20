import json
import hashlib
import re
import os

class Registration():
    def __init__(self):
        self.username = ""
        self.password = ""
        self.password2 = ""
        self.email = ""
        self.username_pattern = re.compile("^[a-zA-Z0-9_]{3,20}$")
        self.password_pattern = re.compile("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")
        self.email_pattern = re.compile("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    
    def register(self):
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
        
        # Get the path to the parent directory of the directory containing auth.py
        parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

        # Construct the path to login.json
        json_path = os.path.join(parent_dir, "files", "login.json")

        try:
            with open(json_path, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            # If the file doesn't exist, create an empty dictionary
            data = {}
        
        if self.username in data:
            print("Username already exists. Please choose a different username.")
            return
        
        data[self.username] = {"password": hashlib.sha256(self.password.encode()).hexdigest(), "email": self.email}
        
        with open("files\login.json", "w") as f:
            json.dump(data, f)
        
        print("Registration successful.")

class Login():
    def __init__(self):
        self.username = ""
        self.password = ""
    
    def login(self):
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
