import unittest
from unittest.mock import patch
import tkinter as tk
import todolistGUI

class TestToDoListGUI(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()

    def tearDown(self):
        self.root.destroy()

    @patch('todolist.add_task')
    def test_add_task(self, mock_add_task):
        # Create the GUI
        todolistGUI.todolistGUI()

        # Simulate user input
        task_entry = self.root.children['.!frame.!entry']
        task_entry.insert(tk.END, 'Task 1')

        description_entry = self.root.children['.!frame.!entry2']
        description_entry.insert(tk.END, 'Description 1')

        deadline_entry = self.root.children['.!frame.!entry3']
        deadline_entry.insert(tk.END, '2022-01-01')

        add_button = self.root.children['.!frame.!button']
        add_button.invoke()

        # Check if the add_task function was called with the correct arguments
        mock_add_task.assert_called_once_with('Task 1', 'Description 1', '2022-01-01')

    @patch('todolist.view_all_tasks')
    def test_view_all_tasks(self, mock_view_all_tasks):
        # Create the GUI
        todolistGUI.todolistGUI()

        # Simulate user input
        view_button = self.root.children['.!frame.!button']
        view_button.invoke()

        # Check if the view_all_tasks function was called
        mock_view_all_tasks.assert_called_once()

    @patch('todolist.mark_task_as_complete')
    def test_mark_task_as_complete(self, mock_mark_task_as_complete):
        # Create the GUI
        todolistGUI.todolistGUI()

        # Simulate user input
        mark_task_entry = self.root.children['.!frame.!entry']
        mark_task_entry.insert(tk.END, '1')

        mark_button = self.root.children['.!frame.!button']
        mark_button.invoke()

        # Check if the mark_task_as_complete function was called with the correct argument
        mock_mark_task_as_complete.assert_called_once_with(1)

    @patch('todolist.delete_task')
    def test_delete_task(self, mock_delete_task):
        # Create the GUI
        todolistGUI.todolistGUI()

        # Simulate user input
        delete_task_entry = self.root.children['.!frame.!entry']
        delete_task_entry.insert(tk.END, '1')

        delete_button = self.root.children['.!frame.!button']
        delete_button.invoke()

        # Check if the delete_task function was called with the correct argument
        mock_delete_task.assert_called_once_with(1)

if __name__ == '__main__':
    unittest.main()