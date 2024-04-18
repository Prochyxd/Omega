import tkinter as tk
from tkinter import filedialog, messagebox
from log_manager import LogManager

class UserInterface:
    @staticmethod
    def show_guide():
        messagebox.showinfo("Guide", "Guide:\n"
                                     "1) Enter the path to the input file. The input file must be a non-empty text file with the .txt extension.\n"
                                     "2) All the words in the input file and their frequencies in the text will be displayed.\n"
                                     "3) Enter a word from the text file that you want to replace, press Enter.\n"
                                     "4) Enter an abbreviation/shortcut for the word you entered before.\n"
                                     "5) Repeat the previous two steps for other words.\n"
                                     "6) Press Enter without entering a word to finish.\n"
                                     "7) Enter the name of the output file with the .txt extension (e.g., example.txt). The output file will be created in the project directory.\n"
                                     "8) The output file contains compressed text.\n"
                                     "9) Choose whether to print the log or not.")

    @staticmethod
    def get_input_file():
        root = tk.Tk()
        root.withdraw()
        input_file_path = filedialog.askopenfilename(title="Select Input File", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if not input_file_path:
            messagebox.showerror("Error", "No file selected!")
            return None
        else:
            return input_file_path

    @staticmethod
    def get_word_replacements():
        replacements = {}
        while True:
            word = input("Enter the word you want to replace, or press Enter to finish: ")
            if not word:
                break
            abbreviation = input(f"Enter an abbreviation for the word '{word}': ")
            replacements[word] = abbreviation
        return replacements

    @staticmethod
    def get_output_file():
        root = tk.Tk()
        root.withdraw()
        output_file_path = filedialog.asksaveasfilename(title="Save As", defaultextension=".txt", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if not output_file_path:
            messagebox.showerror("Error", "No file selected!")
            return None
        else:
            return output_file_path
