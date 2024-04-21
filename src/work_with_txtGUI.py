# work_with_txtGUI.py
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
from work_with_txt import *

class FileOperationsApp:
    def __init__(self, master):
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
        self.file_path = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if self.file_path:
            messagebox.showinfo("File Selected", f"Selected File: {self.file_path}")

    def read_file_gui(self):
        if self.file_path:
            content = read_file(self.file_path)
            messagebox.showinfo("File Content", content)
        else:
            messagebox.showerror("Error", "No file selected.")

    def write_file_gui(self):
        if self.file_path:
            text = simpledialog.askstring("Text", "Enter the text to write in the file:")
            if text:
                message = write_file(self.file_path, text)
                messagebox.showinfo("Message", message)
        else:
            messagebox.showerror("Error", "No file selected.")

    def delete_file_gui(self):
        if self.file_path:
            message = delete_file(self.file_path)
            messagebox.showinfo("Message", message)
            self.file_path = ""
        else:
            messagebox.showerror("Error", "No file selected.")

    def rename_file_gui(self):
        if self.file_path:
            new_name = simpledialog.askstring("New Name", "Enter the new name of the file:")
            if new_name:
                message = rename_file(self.file_path, new_name)
                messagebox.showinfo("Message", message)
                self.file_path = new_name
        else:
            messagebox.showerror("Error", "No file selected.")

    def copy_file_gui(self):
        if self.file_path:
            new_path = simpledialog.askstring("New Path", "Enter the new path of the file:")
            if new_path:
                message = copy_file(self.file_path, new_path)
                messagebox.showinfo("Message", message)
        else:
            messagebox.showerror("Error", "No file selected.")

    def move_file_gui(self):
        if self.file_path:
            new_path = simpledialog.askstring("New Path", "Enter the new path of the file:")
            if new_path:
                message = move_file(self.file_path, new_path)
                messagebox.showinfo("Message", message)
                self.file_path = new_path
        else:
            messagebox.showerror("Error", "No file selected.")

    def add_text_gui(self):
        if self.file_path:
            text = simpledialog.askstring("Text", "Enter the text to add in the file:")
            if text:
                message = add_text(self.file_path, text)
                messagebox.showinfo("Message", message)
        else:
            messagebox.showerror("Error", "No file selected.")

    def count_words_gui(self):
        if self.file_path:
            message = count_words(self.file_path)
            messagebox.showinfo("Message", message)
        else:
            messagebox.showerror("Error", "No file selected.")

    def count_lines_gui(self):
        if self.file_path:
            message = count_lines(self.file_path)
            messagebox.showinfo("Message", message)
        else:
            messagebox.showerror("Error", "No file selected.")

    def count_characters_gui(self):
        if self.file_path:
            message = count_characters(self.file_path)
            messagebox.showinfo("Message", message)
        else:
            messagebox.showerror("Error", "No file selected.")

    def count_special_characters_gui(self):
        if self.file_path:
            message = count_special_characters(self.file_path)
            messagebox.showinfo("Message", message)
        else:
            messagebox.showerror("Error", "No file selected.")

    def count_digits_gui(self):
        if self.file_path:
            message = count_digits(self.file_path)
            messagebox.showinfo("Message", message)
        else:
            messagebox.showerror("Error", "No file selected.")

    def count_spaces_gui(self):
        if self.file_path:
            message = count_spaces(self.file_path)
            messagebox.showinfo("Message", message)
        else:
            messagebox.showerror("Error", "No file selected.")

def run_work_with_txtGUI():
    root = tk.Tk()
    app = FileOperationsApp(root)
    root.mainloop()

