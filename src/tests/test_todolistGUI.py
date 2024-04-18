import unittest
from unittest.mock import patch, MagicMock
import tkinter as tk
import todolistGUI

class TestAddTask(unittest.TestCase):
    @patch('todolistGUI.task_entry.get', return_value="Buy groceries")
    @patch('todolistGUI.description_entry.get', return_value="Buy milk, eggs, and bread")
    @patch('todolistGUI.deadline_entry.get', return_value="2022-12-31")
    @patch('todolistGUI.todolist.add_task')
    def test_add_task_with_all_parameters(self, mock_add_task, mock_deadline_entry, mock_description_entry, mock_task_entry):
        expected_output = "Task added successfully."
        result_label = MagicMock()
        todolistGUI.add_task(result_label)
        mock_add_task.assert_called_once_with("Buy groceries", "Buy milk, eggs, and bread", "2022-12-31")
        result_label.config.assert_called_once_with(text=expected_output)

    @patch('todolistGUI.task_entry.get', return_value="Clean the house")
    @patch('todolistGUI.description_entry.get', return_value="")
    @patch('todolistGUI.deadline_entry.get', return_value="")
    @patch('todolistGUI.todolist.add_task')
    def test_add_task_without_optional_parameters(self, mock_add_task, mock_deadline_entry, mock_description_entry, mock_task_entry):
        expected_output = "Task added successfully."
        result_label = MagicMock()
        todolistGUI.add_task(result_label)
        mock_add_task.assert_called_once_with("Clean the house", "", "")
        result_label.config.assert_called_once_with(text=expected_output)

    @patch('todolistGUI.task_entry.get', return_value="")
    @patch('todolistGUI.description_entry.get', return_value="")
    @patch('todolistGUI.deadline_entry.get', return_value="")
    def test_add_task_with_empty_task_name(self, mock_deadline_entry, mock_description_entry, mock_task_entry):
        expected_output = "Please enter a task and deadline."
        result_label = MagicMock()
        todolistGUI.add_task(result_label)
        result_label.config.assert_called_once_with(text=expected_output)

class TestViewAllTasks(unittest.TestCase):
    @patch('todolistGUI.todolist.view_all_tasks', return_value=[{"task": "Buy groceries", "completed": False, "description": "Buy milk, eggs, and bread", "deadline": "2022-12-31"}])
    def test_view_all_tasks_with_tasks(self, mock_view_all_tasks):
        tasks_text = MagicMock()
        todolistGUI.view_all_tasks(tasks_text)
        tasks_text.delete.assert_called_once_with("1.0", tk.END)
        tasks_text.insert.assert_called_once_with(tk.END, "All tasks:\n1. Buy groceries - Not Completed\n   Description: Buy milk, eggs, and bread\n   Deadline: 2022-12-31\n")

    @patch('todolistGUI.todolist.view_all_tasks', return_value=[])
    def test_view_all_tasks_without_tasks(self, mock_view_all_tasks):
        tasks_text = MagicMock()
        todolistGUI.view_all_tasks(tasks_text)
        tasks_text.delete.assert_called_once_with("1.0", tk.END)
        tasks_text.insert.assert_called_once_with(tk.END, "No tasks found.")

class TestMarkTaskAsComplete(unittest.TestCase):
    @patch('todolistGUI.mark_task_entry.get', return_value="1")
    @patch('todolistGUI.todolist.mark_task_as_complete', return_value=True)
    def test_mark_task_as_complete_with_valid_task_number(self, mock_mark_task_as_complete, mock_mark_task_entry):
        expected_output = "Task marked as complete."
        result_label = MagicMock()
        todolistGUI.mark_task_as_complete(result_label)
        mock_mark_task_as_complete.assert_called_once_with(1)
        result_label.config.assert_called_once_with(text=expected_output)

    @patch('todolistGUI.mark_task_entry.get', return_value="invalid")
    def test_mark_task_as_complete_with_invalid_task_number(self, mock_mark_task_entry):
        expected_output = "Please enter a valid task number."
        result_label = MagicMock()
        todolistGUI.mark_task_as_complete(result_label)
        result_label.config.assert_called_once_with(text=expected_output)

class TestDeleteTask(unittest.TestCase):
    @patch('todolistGUI.delete_task_entry.get', return_value="1")
    @patch('todolistGUI.todolist.delete_task', return_value=True)
    def test_delete_task_with_valid_task_number(self, mock_delete_task, mock_delete_task_entry):
        expected_output = "Task deleted successfully."
        result_label = MagicMock()
        todolistGUI.delete_task(result_label)
        mock_delete_task.assert_called_once_with(1)
        result_label.config.assert_called_once_with(text=expected_output)

    @patch('todolistGUI.delete_task_entry.get', return_value="invalid")
    def test_delete_task_with_invalid_task_number(self, mock_delete_task_entry):
        expected_output = "Please enter a valid task number."
        result_label = MagicMock()
        todolistGUI.delete_task(result_label)
        result_label.config.assert_called_once_with(text=expected_output)

if __name__ == '__main__':
    unittest.main()
