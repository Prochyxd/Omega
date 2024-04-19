import unittest
from unittest.mock import mock_open, patch, MagicMock
import tkinter as tk
from tkinter import messagebox, filedialog
from compressionGUI import CompressionGUI

class TestCompressionGUI(unittest.TestCase):
    def setUp(self):
        self.app = CompressionGUI()

    def test_create_widgets(self):
        self.assertIsInstance(self.app.show_guide_button, tk.Button)
        self.assertIsInstance(self.app.input_file_button, tk.Button)
        self.assertIsInstance(self.app.word_display_label, tk.Label)
        self.assertIsInstance(self.app.word_display_text, tk.Text)
        self.assertIsInstance(self.app.replace_button, tk.Button)
        self.assertIsInstance(self.app.output_file_button, tk.Button)
        self.assertIsInstance(self.app.compress_button, tk.Button)

    @patch('tkinter.messagebox.showinfo')
    @patch('tkinter.filedialog.askopenfilename')
    def test_get_input_file(self, mock_askopenfilename, mock_showinfo):
        mock_askopenfilename.return_value = "/path/to/input.txt"
        self.app.get_input_file()
        mock_askopenfilename.assert_called_once_with(filetypes=[("Text files", "*.txt")])
        mock_showinfo.assert_called_once_with("Success", "Selected input file: /path/to/input.txt")

    @patch('tkinter.messagebox.showinfo')
    @patch('tkinter.filedialog.asksaveasfilename')
    def test_get_output_file(self, mock_asksaveasfilename, mock_showinfo):
        mock_asksaveasfilename.return_value = "/path/to/output.txt"
        self.app.get_output_file()
        mock_asksaveasfilename.assert_called_once_with(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        mock_showinfo.assert_called_once_with("Success", "Selected output file: /path/to/output.txt")

    @patch('tkinter.messagebox.showerror')
    def test_compress_text_no_input_file(self, mock_showerror):
        self.app.input_file_path = ""
        self.app.compress_text()
        mock_showerror.assert_called_once_with("Error", "Please select an input file.")

    @patch('tkinter.messagebox.showerror')
    def test_compress_text_no_output_file(self, mock_showerror):
        self.app.input_file_path = "/path/to/input.txt"
        self.app.output_file_path = ""
        self.app.compress_text()
        mock_showerror.assert_called_once_with("Error", "Please select an output file.")

    @patch('tkinter.messagebox.showerror')
    def test_compress_text_no_replacements(self, mock_showerror):
        self.app.input_file_path = "/path/to/input.txt"
        self.app.output_file_path = "/path/to/output.txt"
        self.app.replacements = {}
        self.app.compress_text()
        mock_showerror.assert_called_once_with("Error", "Please replace at least one word.")

    @patch('tkinter.messagebox.showerror')
    @patch('builtins.open', new_callable=mock_open, read_data="input text")
    def test_compress_text_input_file_not_found(self, mock_open, mock_showerror):
        self.app.input_file_path = "/path/to/nonexistent.txt"
        self.app.output_file_path = "/path/to/output.txt"
        self.app.replacements = {"word": "abbr"}
        self.app.compress_text()
        mock_showerror.assert_called_once_with("Error", "Input file not found.")

    @patch('tkinter.messagebox.showerror')
    @patch('builtins.open', new_callable=mock_open, read_data="input text")
    def test_compress_text_error_reading_input_file(self, mock_open, mock_showerror):
        mock_open.side_effect = Exception("Error reading input file")
        self.app.input_file_path = "/path/to/input.txt"
        self.app.output_file_path = "/path/to/output.txt"
        self.app.replacements = {"word": "abbr"}
        self.app.compress_text()
        mock_showerror.assert_called_once_with("Error", "Error reading input file: Error reading input file")

    @patch('tkinter.messagebox.showerror')
    @patch('builtins.open', new_callable=mock_open, read_data="input text")
    @patch('compressionGUI.LogManager.log_activity')
    @patch('builtins.open', new_callable=mock_open, read_data="input text")
    def test_compress_text_success(self, mock_open1, mock_log_activity, mock_open2, mock_showinfo):
        mock_open1.return_value = MagicMock(spec=open)
        mock_open2.return_value = MagicMock(spec=open)
        self.app.input_file_path = "/path/to/input.txt"
        self.app.output_file_path = "/path/to/output.txt"
        self.app.replacements = {"word": "abbr"}
        self.app.compress_text()
        mock_showinfo.assert_called_once_with("Success", "Text compression successful!")

if __name__ == '__main__':
    unittest.main()