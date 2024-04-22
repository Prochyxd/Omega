import tkinter as tk
from tkinter import messagebox
import datetime

class LogManagerGUI:
    """
    A graphical user interface for managing log activities.

    Args:
        master: The root Tkinter window.

    Attributes:
        master: The root Tkinter window.
        frame: The main frame of the GUI.
        action_label: A label for the action entry field.
        action_entry: An entry field for entering the action.
        details_label: A label for the details entry field.
        details_entry: An entry field for entering the details.
        log_button: A button for adding log activity.
        print_button: A button for printing the log.

    Methods:
        __init__: Initializes the LogManagerGUI instance.
        log_activity: Logs the activity to a file.
        print_log: Prints the contents of the log file.
    """

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
        """
        Logs the activity to a file.

        Retrieves the action and details entered by the user,
        appends the log entry to the log file, and displays a
        success message if the activity is logged successfully.
        Otherwise, displays an error message.
        """
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
        """
        Prints the contents of the log file.

        Reads the log file and displays its contents in a message box.
        Displays an error message if the log file is not found or if
        there is an error while reading the file.
        """
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

