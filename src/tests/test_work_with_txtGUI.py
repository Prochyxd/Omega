import unittest
from unittest.mock import patch
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
from work_with_txtGUI import FileOperationsApp
import tkinter as tk

class TestFileOperationsApp(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = FileOperationsApp(self.root)

    def tearDown(self):
        self.root.destroy()

    @patch.object(filedialog, 'askopenfilename')
    @patch.object(messagebox, 'showinfo')
    def test_choose_file(self, mock_showinfo, mock_askopenfilename):
        mock_askopenfilename.return_value = "/path/to/file.txt"
        self.app.choose_file()
        mock_askopenfilename.assert_called_once_with(initialdir="/", title="Select File", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        mock_showinfo.assert_called_once_with("File Selected", "Selected File: /path/to/file.txt")

    @patch.object(messagebox, 'showerror')
    def test_read_file_gui_no_file_selected(self, mock_showerror):
        self.app.read_file_gui()
        mock_showerror.assert_called_once_with("Error", "No file selected.")

    @patch.object(messagebox, 'showinfo')
    @patch('work_with_txtGUI.read_file')
    def test_read_file_gui_with_file_selected(self, mock_read_file, mock_showinfo):
        self.app.file_path = "/path/to/file.txt"
        mock_read_file.return_value = "File content"
        self.app.read_file_gui()
        mock_read_file.assert_called_once_with("/path/to/file.txt")
        mock_showinfo.assert_called_once_with("File Content", "File content")

    @patch.object(messagebox, 'showerror')
    def test_write_file_gui_no_file_selected(self, mock_showerror):
        self.app.write_file_gui()
        mock_showerror.assert_called_once_with("Error", "No file selected.")

    @patch.object(messagebox, 'showinfo')
    @patch.object(simpledialog, 'askstring')
    @patch('work_with_txtGUI.write_file')
    def test_write_file_gui_with_file_selected(self, mock_write_file, mock_askstring, mock_showinfo):
        self.app.file_path = "/path/to/file.txt"
        mock_askstring.return_value = "New content"
        mock_write_file.return_value = "Text written to file"
        self.app.write_file_gui()
        mock_askstring.assert_called_once_with("Text", "Enter the text to write in the file:")
        mock_write_file.assert_called_once_with("/path/to/file.txt", "New content")
        mock_showinfo.assert_called_once_with("Message", "Text written to file")

    @patch.object(messagebox, 'showerror')
    def test_delete_file_gui_no_file_selected(self, mock_showerror):
        self.app.delete_file_gui()
        mock_showerror.assert_called_once_with("Error", "No file selected.")

    @patch.object(messagebox, 'showinfo')
    @patch('work_with_txtGUI.delete_file')
    def test_delete_file_gui_with_file_selected(self, mock_delete_file, mock_showinfo):
        self.app.file_path = "/path/to/file.txt"
        mock_delete_file.return_value = "File deleted"
        self.app.delete_file_gui()
        mock_delete_file.assert_called_once_with("/path/to/file.txt")
        mock_showinfo.assert_called_once_with("Message", "File deleted")

    @patch.object(messagebox, 'showerror')
    def test_rename_file_gui_no_file_selected(self, mock_showerror):
        self.app.rename_file_gui()
        mock_showerror.assert_called_once_with("Error", "No file selected.")

    @patch.object(messagebox, 'showinfo')
    @patch.object(simpledialog, 'askstring')
    @patch('work_with_txtGUI.rename_file')
    def test_rename_file_gui_with_file_selected(self, mock_rename_file, mock_askstring, mock_showinfo):
        self.app.file_path = "/path/to/file.txt"
        mock_askstring.return_value = "new_file.txt"
        mock_rename_file.return_value = "File renamed"
        self.app.rename_file_gui()
        mock_askstring.assert_called_once_with("New Name", "Enter the new name of the file:")
        mock_rename_file.assert_called_once_with("/path/to/file.txt", "new_file.txt")
        mock_showinfo.assert_called_once_with("Message", "File renamed")


if __name__ == "__main__":
    unittest.main()