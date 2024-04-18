import unittest
from unittest.mock import patch
from io import StringIO
from todolistUI import add_task, view_all_tasks, mark_task_as_complete, delete_task, todo

class TestAddTask(unittest.TestCase):
    def test_add_task(self):
        # Test case 1: Adding a task with all optional parameters
        task = "Buy groceries"
        description = "Buy milk, eggs, and bread"
        deadline = "2022-12-31"
        expected_output = "Task added successfully."
        self.assertEqual(add_task(task, description, deadline), expected_output)

        # Test case 2: Adding a task without optional parameters
        task = "Clean the house"
        expected_output = "Task added successfully."
        self.assertEqual(add_task(task), expected_output)

        # Test case 3: Adding a task with empty task name
        task = ""
        expected_output = "Task added successfully."
        self.assertEqual(add_task(task), expected_output)

        # Test case 4: Adding a task with empty description and deadline
        task = "Walk the dog"
        description = ""
        deadline = ""
        expected_output = "Task added successfully."
        self.assertEqual(add_task(task, description, deadline), expected_output)

class TestViewAllTasks(unittest.TestCase):
    def test_view_all_tasks_with_tasks(self):
        # Test case 1: Viewing all tasks when there are tasks
        tasks = ["Buy groceries", "Clean the house", "Walk the dog"]
        expected_output = "\n".join(tasks)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            view_all_tasks(tasks)
            self.assertEqual(fake_out.getvalue().strip(), expected_output)

    def test_view_all_tasks_without_tasks(self):
        # Test case 2: Viewing all tasks when there are no tasks
        tasks = []
        expected_output = "No tasks found."
        with patch('sys.stdout', new=StringIO()) as fake_out:
            view_all_tasks(tasks)
            self.assertEqual(fake_out.getvalue().strip(), expected_output)

class TestMarkTaskAsComplete(unittest.TestCase):
    def test_mark_task_as_complete(self):
        # Test case 1: Marking a task as complete
        task = "Buy groceries"
        tasks = ["Buy groceries", "Clean the house", "Walk the dog"]
        expected_output = "Task marked as complete."
        self.assertEqual(mark_task_as_complete(task, tasks), expected_output)

        # Test case 2: Marking a task as complete that does not exist
        task = "Do laundry"
        tasks = ["Buy groceries", "Clean the house", "Walk the dog"]
        expected_output = "Task not found."
        self.assertEqual(mark_task_as_complete(task, tasks), expected_output)

class TestDeleteTask(unittest.TestCase):
    def test_delete_task(self):
        # Test case 1: Deleting a task
        task = "Buy groceries"
        tasks = ["Buy groceries", "Clean the house", "Walk the dog"]
        expected_output = "Task deleted successfully."
        self.assertEqual(delete_task(task, tasks), expected_output)

        # Test case 2: Deleting a task that does not exist
        task = "Do laundry"
        tasks = ["Buy groceries", "Clean the house", "Walk the dog"]
        expected_output = "Task not found."
        self.assertEqual(delete_task(task, tasks), expected_output)

class TestTodo(unittest.TestCase):
    @patch('builtins.input', side_effect=["1", "5"])
    def test_todo(self, mock_input):
        # Test case 1: Choosing option 1 and then option 5 to exit
        expected_output = "Choose an option:\n1. Add a task\n2. View all tasks\n3. Mark task as complete\n4. Delete a task\n5. Exit\nEnter your choice: "
        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo()
            self.assertEqual(fake_out.getvalue(), expected_output)

        # Test case 2: Choosing an invalid option and then option 5 to exit
        expected_output = "Choose an option:\n1. Add a task\n2. View all tasks\n3. Mark task as complete\n4. Delete a task\n5. Exit\nEnter your choice: Invalid choice. Please enter a number between 1 and 5."
        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo()
            self.assertEqual(fake_out.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
