import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
from work_with_txt import *

class FileOperationsApp:
    def __init__(self, master):
        """
        Initializes the FileOperationsGUI class.

        Parameters:
        - master: The master widget (typically a Tk or Toplevel instance) that will contain the GUI.

        Returns:
        None
        """
        self.master = master
        self.master.title("File Operations")
        self.master.geometry("600x400")
        
        self.file_path = ""

        self.btn_choose_file = tk.Button(master, text="Choose File", command=self.choose_file)
        self.btn_choose_file.pack()

        self.btn_read_file = tk.Button(master, text="Read File", command=self.read_file_gui)
        self.btn_read_file.pack()

        self.btn_write_file = tk.Button(master, text="Write File", command=self.write_file_gui)
        self.btn_write_file.pack()

        self.btn_delete_file = tk.Button(master, text="Delete File", command=self.delete_file_gui)
        self.btn_delete_file.pack()

        self.btn_rename_file = tk.Button(master, text="Rename File", command=self.rename_file_gui)
        self.btn_rename_file.pack()

        self.btn_copy_file = tk.Button(master, text="Copy File", command=self.copy_file_gui)
        self.btn_copy_file.pack()

        self.btn_move_file = tk.Button(master, text="Move File", command=self.move_file_gui)
        self.btn_move_file.pack()

        self.btn_add_text = tk.Button(master, text="Add Text to File", command=self.add_text_gui)
        self.btn_add_text.pack()

        self.btn_count_words = tk.Button(master, text="Count Words", command=self.count_words_gui)
        self.btn_count_words.pack()

        self.btn_count_lines = tk.Button(master, text="Count Lines", command=self.count_lines_gui)
        self.btn_count_lines.pack()

        self.btn_count_characters = tk.Button(master, text="Count Characters", command=self.count_characters_gui)
        self.btn_count_characters.pack()

        self.btn_count_special_characters = tk.Button(master, text="Count Special Characters", command=self.count_special_characters_gui)
        self.btn_count_special_characters.pack()

        self.btn_count_digits = tk.Button(master, text="Count Digits", command=self.count_digits_gui)
        self.btn_count_digits.pack()

        self.btn_count_spaces = tk.Button(master, text="Count Spaces", command=self.count_spaces_gui)
        self.btn_count_spaces.pack()

    def choose_file(self):
        """
        Opens a file dialog to allow the user to select a text file.
        Updates the `file_path` attribute with the selected file path.
        Displays a message box with the selected file path if a file is selected.
        """
        self.file_path = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if self.file_path:
            messagebox.showinfo("File Selected", f"Selected File: {self.file_path}")

    def read_file_gui(self):
        """
        Reads the content of a file and displays it in a message box.

        If a file path is selected, the method reads the content of the file
        using the `read_file` function and displays it in a message box with
        the title "File Content". If no file path is selected, an error message
        box with the title "Error" is displayed.

        Args:
            self: The instance of the class.

        Returns:
            None
        """
        if self.file_path:
            content = read_file(self.file_path)
            messagebox.showinfo("File Content", content)
        else:
            messagebox.showerror("Error", "No file selected.")

    def write_file_gui(self):
        """
        Writes the provided text to the selected file.

        If a file is selected, the method prompts the user to enter the text to write in the file.
        If the user provides a non-empty text, the method calls the `write_file` function to write the text to the file.
        Finally, it displays a message box with the result of the write operation.

        If no file is selected, an error message is displayed.

        Parameters:
        - self: The current instance of the class.

        Returns:
        None
        """
        if self.file_path:
            text = simpledialog.askstring("Text", "Enter the text to write in the file:")
            if text:
                message = write_file(self.file_path, text)
                messagebox.showinfo("Message", message)
        else:
            messagebox.showerror("Error", "No file selected.")

    def delete_file_gui(self):
            """
            Deletes the selected file and displays a message box with the result.

            If a file is selected, it calls the `delete_file` function passing the file path as an argument.
            The returned message is then displayed in an information message box.
            If no file is selected, an error message box is displayed.

            Args:
                self: The instance of the class.

            Returns:
                None
            """
            if self.file_path:
                message = delete_file(self.file_path)
                messagebox.showinfo("Message", message)
                self.file_path = ""
            else:
                messagebox.showerror("Error", "No file selected.")

    def rename_file_gui(self):
        """
        Renames the selected file.

        If a file is selected, prompts the user to enter a new name for the file.
        If a new name is provided, renames the file and displays a message box with the result.
        If no file is selected, displays an error message.

        Args:
            self: The instance of the class.

        Returns:
            None
        """
        if self.file_path:
            new_name = simpledialog.askstring("New Name", "Enter the new name of the file:")
            if new_name:
                message = rename_file(self.file_path, new_name)
                messagebox.showinfo("Message", message)
                self.file_path = new_name
        else:
            messagebox.showerror("Error", "No file selected.")

    def copy_file_gui(self):
            """
            Copies the selected file to a new location specified by the user.

            If a file is selected, the method prompts the user to enter a new path for the file.
            If a new path is provided, the method calls the `copy_file` function to copy the file to the new location.
            Finally, it displays a message box with the result of the copy operation.

            If no file is selected, an error message is displayed.

            Args:
                self: The current instance of the class.

            Returns:
                None
            """
            if self.file_path:
                new_path = simpledialog.askstring("New Path", "Enter the new path of the file:")
                if new_path:
                    message = copy_file(self.file_path, new_path)
                    messagebox.showinfo("Message", message)
            else:
                messagebox.showerror("Error", "No file selected.")

    def move_file_gui(self):
        """
        Moves the selected file to a new location specified by the user.

        If a file is selected, the method prompts the user to enter the new path of the file.
        If a new path is provided, the method calls the `move_file` function to move the file to the new location.
        After moving the file, a message box is displayed with the result of the operation.
        If no file is selected, an error message is displayed.

        Parameters:
        - self: The current instance of the class.

        Returns:
        None
        """
        if self.file_path:
            new_path = simpledialog.askstring("New Path", "Enter the new path of the file:")
            if new_path:
                message = move_file(self.file_path, new_path)
                messagebox.showinfo("Message", message)
                self.file_path = new_path
        else:
            messagebox.showerror("Error", "No file selected.")

    def add_text_gui(self):
        """
        Adds text to a file selected by the user.

        If a file is selected, it prompts the user to enter the text to add in the file.
        If the user enters text, it calls the `add_text` function to add the text to the file.
        Finally, it displays a message box with the result of the operation.

        Raises:
            None

        Returns:
            None
        """
        if self.file_path:
            text = simpledialog.askstring("Text", "Enter the text to add in the file:")
            if text:
                message = add_text(self.file_path, text)
                messagebox.showinfo("Message", message)
        else:
            messagebox.showerror("Error", "No file selected.")

    def count_words_gui(self):
        """
        Counts the number of words in a selected file and displays the result in a message box.

        If a file is selected, the method calls the `count_words` function passing the file path as an argument.
        The returned message is then displayed in an information message box.
        If no file is selected, an error message box is displayed.

        Parameters:
        - self: The instance of the class.

        Returns:
        - None
        """
        if self.file_path:
            message = count_words(self.file_path)
            messagebox.showinfo("Message", message)
        else:
            messagebox.showerror("Error", "No file selected.")

    def count_lines_gui(self):
        """
        Counts the number of lines in the selected file and displays the result in a message box.

        If a file is selected, the method calls the `count_lines` function passing the file path as an argument.
        The returned message is then displayed in an information message box.
        If no file is selected, an error message box is displayed.

        Args:
            self: The instance of the class.

        Returns:
            None
        """
        if self.file_path:
            message = count_lines(self.file_path)
            messagebox.showinfo("Message", message)
        else:
            messagebox.showerror("Error", "No file selected.")

    def count_characters_gui(self):
        """
        Displays a message box with the count of characters in the selected file.

        If a file is selected, it calls the `count_characters` function passing the file path as an argument.
        The returned message is then displayed in an information message box.
        If no file is selected, it displays an error message.

        Args:
            self: The instance of the class.

        Returns:
            None
        """
        if self.file_path:
            message = count_characters(self.file_path)
            messagebox.showinfo("Message", message)
        else:
            messagebox.showerror("Error", "No file selected.")

    def count_special_characters_gui(self):
        """
        Displays a message box with the count of special characters in the selected file.

        If a file is selected, it calls the `count_special_characters` function passing the file path as an argument.
        The returned message is then displayed in an information message box.
        If no file is selected, it displays an error message.

        Args:
            self: The instance of the class.

        Returns:
            None
        """
        if self.file_path:
            message = count_special_characters(self.file_path)
            messagebox.showinfo("Message", message)
        else:
            messagebox.showerror("Error", "No file selected.")

    def count_digits_gui(self):
        """
        Displays a message box with the count of digits in the selected file.

        If a file is selected, it calls the `count_digits` function passing the file path as an argument.
        The returned count is then displayed in a message box with the title "Message".
        If no file is selected, it displays an error message box with the title "Error".
        """
        if self.file_path:
            message = count_digits(self.file_path)
            messagebox.showinfo("Message", message)
        else:
            messagebox.showerror("Error", "No file selected.")

    def count_spaces_gui(self):
        """
        Counts the number of spaces in the selected file and displays a message box with the result.

        If a file is selected, the method calls the `count_spaces` function passing the file path as an argument.
        The returned message is then displayed in an information message box.
        If no file is selected, an error message box is displayed.

        Parameters:
        - self: The instance of the class.

        Returns:
        - None
        """
        if self.file_path:
            message = count_spaces(self.file_path)
            messagebox.showinfo("Message", message)
        else:
            messagebox.showerror("Error", "No file selected.")

def run_work_with_txtGUI():
    root = tk.Tk()
    app = FileOperationsApp(root)
    root.mainloop()

