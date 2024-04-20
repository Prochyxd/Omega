import tkinter as tk
from tkinter import messagebox
from .auth import Registration, Login

class AuthenticationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Authentication System")
        self.root.geometry("300x150")
        
        self.registration = Registration()
        self.login = Login()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Welcome to Authentication System", font=("Arial", 12)).pack(pady=10)
        
        tk.Button(self.root, text="Login", command=self.show_login_window).pack()
        tk.Button(self.root, text="Register", command=self.show_registration_window).pack()

    def show_login_window(self):
        login_window = tk.Toplevel(self.root)
        login_window.title("Login")
        login_window.geometry("250x120")

        tk.Label(login_window, text="Username:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(login_window, text="Password:").grid(row=1, column=0, padx=5, pady=5)

        username_entry = tk.Entry(login_window)
        password_entry = tk.Entry(login_window, show="*")
        username_entry.grid(row=0, column=1, padx=5, pady=5)
        password_entry.grid(row=1, column=1, padx=5, pady=5)

        def login():
            username = username_entry.get()
            password = password_entry.get()
            if self.login.authenticate(username, password):
                messagebox.showinfo("Success", "Login successful")
            else:
                messagebox.showerror("Error", "Invalid username or password")
                username_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)

        tk.Button(login_window, text="Login", command=login).grid(row=2, column=1, padx=5, pady=5)

    def show_registration_window(self):
        registration_window = tk.Toplevel(self.root)
        registration_window.title("Register")
        registration_window.geometry("250x200")

        tk.Label(registration_window, text="Username:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(registration_window, text="Password:").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(registration_window, text="Confirm Password:").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(registration_window, text="Email:").grid(row=3, column=0, padx=5, pady=5)

        username_entry = tk.Entry(registration_window)
        password_entry = tk.Entry(registration_window, show="*")
        confirm_password_entry = tk.Entry(registration_window, show="*")
        email_entry = tk.Entry(registration_window)
        username_entry.grid(row=0, column=1, padx=5, pady=5)
        password_entry.grid(row=1, column=1, padx=5, pady=5)
        confirm_password_entry.grid(row=2, column=1, padx=5, pady=5)
        email_entry.grid(row=3, column=1, padx=5, pady=5)

        def register():
            username = username_entry.get()
            password = password_entry.get()
            confirm_password = confirm_password_entry.get()
            email = email_entry.get()
            if password != confirm_password:
                messagebox.showerror("Error", "Passwords do not match")
                password_entry.delete(0, tk.END)
                confirm_password_entry.delete(0, tk.END)
                return
            if self.registration.register(username, password, email):
                messagebox.showinfo("Success", "Registration successful")
                registration_window.destroy()
            else:
                messagebox.showerror("Error", "Username already exists")
                username_entry.delete(0, tk.END)

        tk.Button(registration_window, text="Register", command=register).grid(row=4, column=1, padx=5, pady=5)

def run_auth_gui():
    root = tk.Tk()
    app = AuthenticationGUI(root)
    root.mainloop()
