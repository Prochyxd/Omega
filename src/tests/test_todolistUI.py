import unittest
from unittest.mock import patch
import io
import sys
import todolistUI

class TestToDoListUI(unittest.TestCase):
    @patch('todolistUI.add_task')
    def test_add_task(self, mock_add_task):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            # Simulate user input
            with patch('builtins.input', side_effect=['1', '5']):
                todolistUI.todo()

            # Check if the add_task function was called
            mock_add_task.assert_called_once()

            # Check if the correct output was printed
            expected_output = "\nChoose an option:\n1. Add a task\n2. View all tasks\n3. Mark task as complete\n4. Delete a task\n5. Exit\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('todolistUI.view_all_tasks')
    def test_view_all_tasks(self, mock_view_all_tasks):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            # Simulate user input
            with patch('builtins.input', side_effect=['2', '5']):
                todolistUI.todo()

            # Check if the view_all_tasks function was called
            mock_view_all_tasks.assert_called_once()

            # Check if the correct output was printed
            expected_output = "\nChoose an option:\n1. Add a task\n2. View all tasks\n3. Mark task as complete\n4. Delete a task\n5. Exit\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('todolistUI.mark_task_as_complete')
    def test_mark_task_as_complete(self, mock_mark_task_as_complete):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            # Simulate user input
            with patch('builtins.input', side_effect=['3', '5']):
                todolistUI.todo()

            # Check if the mark_task_as_complete function was called
            mock_mark_task_as_complete.assert_called_once()

            # Check if the correct output was printed
            expected_output = "\nChoose an option:\n1. Add a task\n2. View all tasks\n3. Mark task as complete\n4. Delete a task\n5. Exit\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('todolistUI.delete_task')
    def test_delete_task(self, mock_delete_task):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            # Simulate user input
            with patch('builtins.input', side_effect=['4', '5']):
                todolistUI.todo()

            # Check if the delete_task function was called
            mock_delete_task.assert_called_once()

    def test_invalid_choice(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            # Simulate user input
            with patch('builtins.input', side_effect=['6', '5']):
                todolistUI.todo()

            # Check if the correct output was printed
            expected_output = "Invalid choice. Please enter a number between 1 and 5.\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

            # Check if the add_task, view_all_tasks, mark_task_as_complete, and delete_task functions were not called
            self.assertFalse(todolistUI.mock_add_task.called)
            self.assertFalse(todolistUI.mock_view_all_tasks.called)
            self.assertFalse(todolistUI.mock_mark_task_as_complete.called)
            self.assertFalse(todolistUI.mock_delete_task.called)

if __name__ == '__main__':
    unittest.main()