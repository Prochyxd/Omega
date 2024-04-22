import tkinter as tk
from tkinter import messagebox, filedialog
from algorithms import WordReplacer
from frequency_analyzer import FrequencyAnalyzer
from log_manager import LogManager

class CompressionGUI(tk.Tk):
    """
    A graphical user interface for a text compression tool.

    This class represents the main window of the text compression tool. It provides
    functionality for selecting input and output files, displaying word frequencies,
    replacing words, and compressing text.

    Attributes:
        input_file_path (str): The path of the selected input file.
        output_file_path (str): The path of the selected output file.
        replacements (dict): A dictionary of word replacements, where the keys are words
            to be replaced and the values are their corresponding abbreviations.

    Methods:
        __init__(): Initializes the CompressionGUI instance.
        create_widgets(): Creates and displays the widgets for the compression GUI.
        show_guide(): Displays a guide for using the compression tool.
        get_input_file(): Opens a file dialog to select an input file.
        get_output_file(): Opens a file dialog to select an output file.
        get_word_replacements(): Opens a window to enter word replacements.
        compress_text(): Compresses the text using the specified word replacements.
    """

    def __init__(self):
        super().__init__()
        self.title("Text Compression Tool")
        self.geometry("600x500")

        self.input_file_path = ""
        self.output_file_path = ""
        self.replacements = {}

        self.create_widgets()

    def create_widgets(self):
        """
        Creates and displays the widgets for the compression GUI.

        This method creates and configures various widgets such as labels, buttons, and text fields
        to be displayed in the compression GUI. It sets up the layout and functionality of the GUI.

        Args:
            self: The instance of the compression GUI.

        Returns:
            None
        """
        tk.Label(self, text="Text Compression Tool", font=("Helvetica", 16)).pack(pady=10)

        self.show_guide_button = tk.Button(self, text="Show Guide", command=self.show_guide)
        self.show_guide_button.pack()

        self.input_file_button = tk.Button(self, text="Select Input File", command=self.get_input_file)
        self.input_file_button.pack(pady=5)

        self.word_display_label = tk.Label(self, text="Words in the input text:")
        self.word_display_label.pack()

        self.word_display_text = tk.Text(self, height=10, width=50)
        self.word_display_text.pack()

        self.replace_button = tk.Button(self, text="Replace Words", command=self.get_word_replacements)
        self.replace_button.pack(pady=5)

        self.output_file_button = tk.Button(self, text="Select Output File", command=self.get_output_file)
        self.output_file_button.pack(pady=5)

        self.compress_button = tk.Button(self, text="Compress Text", command=self.compress_text)
        self.compress_button.pack(pady=10)

    def show_guide(self):
        guide_text = """
        Guide:
    1) Select the input file. It must be a non-empty text file with the .txt extension.
    2) All words in the input file and their frequencies will be displayed.
    3) Enter a word from the text file that you want to replace.
    4) Enter an abbreviation/shortcut for the word you entered before.
    5) Repeat the previous two steps for other words.
    6) Press the Replace Words button to finish.
    7) Select the output file. The compressed text will be saved there.
        """
        messagebox.showinfo("Compression Guide", guide_text)

    def get_input_file(self):
        self.input_file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if self.input_file_path:
            with open(self.input_file_path, "r", encoding="utf-8") as file:
                input_text = file.read()
                self.word_display_text.delete(1.0, tk.END)
                frequency_analyzer = FrequencyAnalyzer()
                word_counts = frequency_analyzer.analyze(input_text)

                sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
                for word, count in sorted_word_counts:
                    self.word_display_text.insert(tk.END, f"{word}: {count}\n")
            messagebox.showinfo("Success", f"Selected input file: {self.input_file_path}")

    def get_output_file(self):
        self.output_file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if self.output_file_path:
            messagebox.showinfo("Success", f"Selected output file: {self.output_file_path}")

    def get_word_replacements(self):
        replacements_window = tk.Toplevel(self)
        replacements_window.title("Word Replacements")
        replacements_window.geometry("400x150")

        tk.Label(replacements_window, text="Enter word to be shorter:").pack()

        word_entry = tk.Entry(replacements_window)
        word_entry.pack(pady=5)

        tk.Label(replacements_window, text="Enter abbreviation:").pack()
        
        abbr_entry = tk.Entry(replacements_window)
        abbr_entry.pack(pady=5)

        def add_replacement():
            word = word_entry.get().strip()
            abbr = abbr_entry.get().strip()
            if word and abbr:
                self.replacements[word] = abbr
                word_entry.delete(0, tk.END)
                abbr_entry.delete(0, tk.END)

        tk.Button(replacements_window, text="Add Replacement", command=add_replacement).pack(pady=5)

    def compress_text(self):
            """
            Compresses the text based on the selected input file, output file, and word replacements.

            Raises:
                FileNotFoundError: If the input file is not found.
                Exception: If there is an error reading the input file or saving the compressed text.

            Returns:
                None
            """
            if not self.input_file_path:
                messagebox.showerror("Error", "Please select an input file.")
                return
            if not self.output_file_path:
                messagebox.showerror("Error", "Please select an output file.")
                return
            if not self.replacements:
                messagebox.showerror("Error", "Please replace at least one word.")
                return

            try:
                with open(self.input_file_path, "r", encoding="utf-8") as file:
                    input_text = file.read()
            except FileNotFoundError:
                messagebox.showerror("Error", "Input file not found.")
                return
            except Exception as e:
                messagebox.showerror("Error", f"Error reading input file: {str(e)}")
                return

            frequency_analyzer = FrequencyAnalyzer()
            word_counts = frequency_analyzer.analyze(input_text)

            replacements_text = "\n".join([f"{word}: {abbr}" for word, abbr in self.replacements.items()])
            action_details = f"Word Replacements:\n{replacements_text}"
            LogManager.log_activity("Word Replacement", action_details)

            word_replacer = WordReplacer(self.replacements)
            compressed_text = word_replacer.replace_words(input_text)

            try:
                with open(self.output_file_path, "w") as file:
                    file.write(compressed_text)
            except Exception as e:
                messagebox.showerror("Error", f"Error saving compressed text: {str(e)}")
                return

            messagebox.showinfo("Success", "Text compression successful!")

def run_compression_gui():
    app = CompressionGUI()
    app.mainloop()
