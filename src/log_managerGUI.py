import tkinter as tk
from tkinter import messagebox
import datetime

class LogManagerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Log Manager")

        self.frame = tk.Frame(master, pady=10)
        self.frame.pack()

        self.action_label = tk.Label(self.frame, text="Action:")
        self.action_label.grid(row=0, column=0, sticky="e")
        self.action_entry = tk.Entry(self.frame)
        self.action_entry.grid(row=0, column=1)

        self.details_label = tk.Label(self.frame, text="Details:")
        self.details_label.grid(row=1, column=0, sticky="e")
        self.details_entry = tk.Entry(self.frame)
        self.details_entry.grid(row=1, column=1)

        self.log_button = tk.Button(self.frame, text="Add Log Activity", command=self.log_activity)
        self.log_button.grid(row=2, columnspan=2, pady=5)

        self.print_button = tk.Button(self.frame, text="Print Log", command=self.print_log)
        self.print_button.grid(row=3, columnspan=2)

    def log_activity(self):
        action = self.action_entry.get()
        details = self.details_entry.get()
        
        try:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"{timestamp} - {action}: {details}\n"
            log_file_path = "log/activity_log.txt"
            with open(log_file_path, "a") as log_file:
                log_file.write(log_entry)
            messagebox.showinfo("Success", "Activity logged successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Error logging activity: {e}")

    def print_log(self):
        try:
            log_file_path = "log/activity_log.txt"
            with open(log_file_path, "r") as log_file:
                log_content = log_file.read()
                messagebox.showinfo("Log Content", log_content)
        except FileNotFoundError:
            messagebox.showerror("Error", "Log file not found.")
        except Exception as e:
            messagebox.showerror("Error", f"Error printing log: {e}")

def run_log_manager_gui():
    root = tk.Tk()
    app = LogManagerGUI(root)
    root.mainloop()

