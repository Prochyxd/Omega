import tkinter as tk
from tkinter import messagebox
import json
import hashlib
import re
import os

class AuthGUI:
    def __init__(self, master):
        self.master = master
        master.title("Authentication")

        self.frame = tk.Frame(master, pady=10)
        self.frame.pack()

        self.username_label = tk.Label(self.frame, text="Username:")
        self.username_label.grid(row=0, column=0, sticky="e")
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.grid(row=0, column=1)

        self.password_label = tk.Label(self.frame, text="Password:")
        self.password_label.grid(row=1, column=0, sticky="e")
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1)

        self.login_button = tk.Button(self.frame, text="Login", command=self.login)
        self.login_button.grid(row=2, columnspan=2, pady=5)

        self.register_button = tk.Button(self.frame, text="Register", command=self.register)
        self.register_button.grid(row=3, columnspan=2)

    def register(self):
        register_window = tk.Toplevel(self.master)
        RegisterGUI(register_window)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        json_path = "files/login.json"

        try:
            with open(json_path, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            messagebox.showerror("Error", "User data file not found.")
            return

        if username not in data:
            messagebox.showerror("Error", "Username not found. Please enter a valid username.")
            return

        if data[username]["password"] == hashlib.sha256(password.encode()).hexdigest():
            messagebox.showinfo("Success", "Login successful.")
            self.master.destroy()
        else:
            messagebox.showerror("Error", "Incorrect password. Please enter a valid password.")

class RegisterGUI:
    def __init__(self, master):
        self.master = master
        master.title("Registration")

        self.frame = tk.Frame(master, pady=10)
        self.frame.pack()

        self.username_label = tk.Label(self.frame, text="Username:")
        self.username_label.grid(row=0, column=0, sticky="e")
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.grid(row=0, column=1)

        self.password_label = tk.Label(self.frame, text="Password:")
        self.password_label.grid(row=1, column=0, sticky="e")
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1)

        self.password2_label = tk.Label(self.frame, text="Re-enter Password:")
        self.password2_label.grid(row=2, column=0, sticky="e")
        self.password2_entry = tk.Entry(self.frame, show="*")
        self.password2_entry.grid(row=2, column=1)

        self.email_label = tk.Label(self.frame, text="Email:")
        self.email_label.grid(row=3, column=0, sticky="e")
        self.email_entry = tk.Entry(self.frame)
        self.email_entry.grid(row=3, column=1)

        self.register_button = tk.Button(self.frame, text="Register", command=self.register)
        self.register_button.grid(row=4, columnspan=2, pady=5)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        password2 = self.password2_entry.get()
        email = self.email_entry.get()

        username_pattern = re.compile("^[a-zA-Z0-9_]{3,20}$")
        password_pattern = re.compile("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")
        email_pattern = re.compile("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

        if not username_pattern.match(username):
            messagebox.showerror("Error", "Invalid username. Please enter a username that is between 3 and 20 characters long and only contains letters, numbers, and underscores.")
            return

        if not password_pattern.match(password):
            messagebox.showerror("Error", "Invalid password. Please enter a password that is at least 8 characters long and contains at least one letter and one number.")
            return

        if password != password2:
            messagebox.showerror("Error", "Passwords do not match. Please re-enter your password.")
            return

        if not email_pattern.match(email):
            messagebox.showerror("Error", "Invalid email address. Please enter a valid email address.")
            return

        json_path = "files/login.json"

        try:
            with open(json_path, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}

        if username in data:
            messagebox.showerror("Error", "Username already exists. Please choose a different username.")
            return

        data[username] = {"password": hashlib.sha256(password.encode()).hexdigest(), "email": email}

        with open(json_path, "w") as f:
            json.dump(data, f)

        messagebox.showinfo("Success", "Registration successful.")
        self.master.destroy()

def run_auth_gui():
    root = tk.Tk()
    app = AuthGUI(root)
    root.mainloop()
