import unittest
from unittest.mock import patch
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
from work_with_txtGUI import FileOperationsApp
import tkinter as tk

class TestFileOperationsApp(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment before each test case.

        This method is called before each individual test case is run. It initializes the root Tkinter
        window and creates an instance of the FileOperationsApp class.

        Args:
            self: The current instance of the test class.

        Returns:
            None
        """
        self.root = tk.Tk()
        self.app = FileOperationsApp(self.root)

    def tearDown(self):
        """
        Clean up method called after each test case.
        Destroys the root GUI window.
        """
        self.root.destroy()

    @patch.object(filedialog, 'askopenfilename')
    @patch.object(messagebox, 'showinfo')
    def test_choose_file(self, mock_showinfo, mock_askopenfilename):
        """
        Test the choose_file method of the application.
        This test verifies that the choose_file method correctly calls the askopenfilename function
        from the filedialog module and shows the selected file information using the showinfo function
        from the messagebox module.
        It mocks the return value of askopenfilename to simulate the selection of a file.
        The assert_called_once_with method is used to check if the askopenfilename function is called
        with the expected arguments.
        The assert_called_once_with method is also used to check if the showinfo function is called
        with the expected arguments.
        """
        mock_askopenfilename.return_value = "/path/to/file.txt"
        self.app.choose_file()
        mock_askopenfilename.assert_called_once_with(initialdir="/", title="Select File", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        mock_showinfo.assert_called_once_with("File Selected", "Selected File: /path/to/file.txt")

    @patch.object(messagebox, 'showerror')
    def test_read_file_gui_no_file_selected(self, mock_showerror):
        """
        Test case for the read_file_gui method when no file is selected.

        This test case verifies that the read_file_gui method displays an error message when no file is selected.

        Args:
            mock_showerror: The mock object for the messagebox.showerror method.

        Returns:
            None
        """
        self.app.read_file_gui()
        mock_showerror.assert_called_once_with("Error", "No file selected.")

    @patch.object(messagebox, 'showinfo')
    @patch('work_with_txtGUI.read_file')
    def test_read_file_gui_with_file_selected(self, mock_read_file, mock_showinfo):
        """
        Test case for the read_file_gui method when a file is selected.
        This test case verifies that the read_file_gui method correctly calls the read_file function
        with the selected file path and displays the file content in a message box.
        Mocks are used to replace the actual read_file function and the showinfo method from the messagebox module.
        Assertions:
        - The read_file function is called once with the selected file path.
        - The showinfo method is called once with the title "File Content" and the file content as the message.
        """
        self.app.file_path = "/path/to/file.txt"
        mock_read_file.return_value = "File content"
        self.app.read_file_gui()
        mock_read_file.assert_called_once_with("/path/to/file.txt")
        mock_showinfo.assert_called_once_with("File Content", "File content")

    @patch.object(messagebox, 'showerror')
    def test_write_file_gui_no_file_selected(self, mock_showerror):
        """
        Test case for the write_file_gui method when no file is selected.

        This test case verifies that the write_file_gui method displays an error message
        when no file is selected.

        Args:
            mock_showerror: The mock object for the messagebox.showerror method.

        Returns:
            None
        """
        self.app.write_file_gui()
        mock_showerror.assert_called_once_with("Error", "No file selected.")

    @patch.object(messagebox, 'showinfo')
    @patch.object(simpledialog, 'askstring')
    @patch('work_with_txtGUI.write_file')
    def test_write_file_gui_with_file_selected(self, mock_write_file, mock_askstring, mock_showinfo):
        """
        Test case for the write_file_gui method when a file is selected.
        This test case verifies that the write_file_gui method correctly interacts with the user interface
        by mocking the necessary functions and asserting the expected calls.
        It sets the file_path attribute of the app to "/path/to/file.txt", mocks the askstring function to
        return "New content", mocks the write_file function to return "Text written to file", and then calls
        the write_file_gui method.
        The test asserts that the askstring function is called with the expected arguments, the write_file
        function is called with the expected arguments, and the showinfo function is called with the expected
        arguments.
        This test case helps ensure that the write_file_gui method behaves as expected when a file is selected.
        """
        self.app.file_path = "/path/to/file.txt"
        mock_askstring.return_value = "New content"
        mock_write_file.return_value = "Text written to file"
        self.app.write_file_gui()
        mock_askstring.assert_called_once_with("Text", "Enter the text to write in the file:")
        mock_write_file.assert_called_once_with("/path/to/file.txt", "New content")
        mock_showinfo.assert_called_once_with("Message", "Text written to file")

    @patch.object(messagebox, 'showerror')
    def test_delete_file_gui_no_file_selected(self, mock_showerror):
        """
        Test case for the delete_file_gui method when no file is selected.

        This test verifies that the delete_file_gui method displays an error message when no file is selected.

        Args:
            mock_showerror: The mock object for the showerror method of the messagebox module.

        Returns:
            None
        """
        self.app.delete_file_gui()
        mock_showerror.assert_called_once_with("Error", "No file selected.")

    @patch.object(messagebox, 'showinfo')
    @patch('work_with_txtGUI.delete_file')
    def test_delete_file_gui_with_file_selected(self, mock_delete_file, mock_showinfo):
        """
        Test case for the delete_file_gui method when a file is selected.
        This test case verifies that the delete_file_gui method correctly calls the delete_file function
        with the selected file path and displays a message box with the appropriate message.
        Args:
            mock_delete_file (MagicMock): A mock object for the delete_file function.
            mock_showinfo (MagicMock): A mock object for the showinfo function.
        Returns:
            None
        """
        self.app.file_path = "/path/to/file.txt"
        mock_delete_file.return_value = "File deleted"
        self.app.delete_file_gui()
        mock_delete_file.assert_called_once_with("/path/to/file.txt")
        mock_showinfo.assert_called_once_with("Message", "File deleted")

    @patch.object(messagebox, 'showerror')
    def test_rename_file_gui_no_file_selected(self, mock_showerror):
        """
        Test case for the rename_file_gui method when no file is selected.

        This test case verifies that the rename_file_gui method displays an error message
        when no file is selected.

        Args:
            mock_showerror: The mock object for the showerror method of the messagebox module.

        Returns:
            None
        """
        self.app.rename_file_gui()
        mock_showerror.assert_called_once_with("Error", "No file selected.")

    @patch.object(messagebox, 'showinfo')
    @patch.object(simpledialog, 'askstring')
    @patch('work_with_txtGUI.rename_file')
    def test_rename_file_gui_with_file_selected(self, mock_rename_file, mock_askstring, mock_showinfo):
        """
        Test case for the rename_file_gui() method when a file is selected.
        This test case verifies that the rename_file_gui() method correctly calls the necessary functions
        and displays the appropriate message box with the result of the file renaming operation.
        It uses the patch decorator to mock the showinfo, askstring, and rename_file functions.
        The file_path attribute of the app object is set to "/path/to/file.txt".
        The mock_askstring function is configured to return "new_file.txt".
        The mock_rename_file function is configured to return "File renamed".
        The rename_file_gui() method is then called and the following assertions are made:
        - mock_askstring is called once with the expected arguments.
        - mock_rename_file is called once with the expected arguments.
        - mock_showinfo is called once with the expected arguments.
        """
        self.app.file_path = "/path/to/file.txt"
        mock_askstring.return_value = "new_file.txt"
        mock_rename_file.return_value = "File renamed"
        self.app.rename_file_gui()
        mock_askstring.assert_called_once_with("New Name", "Enter the new name of the file:")
        mock_rename_file.assert_called_once_with("/path/to/file.txt", "new_file.txt")
        mock_showinfo.assert_called_once_with("Message", "File renamed")


if __name__ == "__main__":
    unittest.main()