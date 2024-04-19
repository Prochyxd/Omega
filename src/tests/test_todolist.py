import unittest
import json
import os
from unittest.mock import patch
from todolist import load_data, save_data, add_task, view_all_tasks, mark_task_as_complete, delete_task

class TestTodoList(unittest.TestCase):

    def setUp(self):
        # Create a test directory and a test data file
        os.makedirs("test_files", exist_ok=True)
        self.test_data_file = "test_files/test_tododata.json"

    def tearDown(self):
        # Clean up the test directory and files
        if os.path.exists(self.test_data_file):
            os.remove(self.test_data_file)
        os.rmdir("test_files")

    def test_load_data_existing_file(self):
        # Create a test data file with some content
        with open(self.test_data_file, "w") as file:
            json.dump([{"task": "Test Task", "description": "Test Description", "deadline": "Test Deadline", "completed": False}], file)

        # Load data from the test data file
        data = load_data()

        # Check if data is loaded correctly
        self.assertEqual(data, [{"task": "Test Task", "description": "Test Description", "deadline": "Test Deadline", "completed": False}])

    def test_load_data_non_existing_file(self):
        # Load data from a non-existing test data file
        data = load_data()

        # Check if empty list is returned
        self.assertEqual(data, [])

    def test_save_data(self):
        # Test saving data to the test data file
        test_data = [{"task": "Test Task", "description": "Test Description", "deadline": "Test Deadline", "completed": False}]
        save_data(test_data)

        # Load saved data from the test data file
        with open(self.test_data_file, "r") as file:
            saved_data = json.load(file)

        # Check if data is saved correctly
        self.assertEqual(saved_data, test_data)

    @patch('builtins.input', side_effect=["Test Task", "Test Description", "Test Deadline"])
    def test_add_task(self, mock_input):
        # Test adding a task with mocked input
        add_task()

        # Load data from the test data file
        with open(self.test_data_file, "r") as file:
            data = json.load(file)

        # Check if task is added correctly
        self.assertEqual(data, [{"task": "Test Task", "description": "Test Description", "deadline": "Test Deadline", "completed": False}])

    def test_view_all_tasks(self):
        # Create a test data file with some content
        with open(self.test_data_file, "w") as file:
            json.dump([{"task": "Test Task", "description": "Test Description", "deadline": "Test Deadline", "completed": False}], file)

        # Test viewing all tasks
        tasks = view_all_tasks()

        # Check if tasks are viewed correctly
        self.assertEqual(tasks, [{"task": "Test Task", "description": "Test Description", "deadline": "Test Deadline", "completed": False}])

    @patch('builtins.input', return_value="1")
    def test_mark_task_as_complete(self, mock_input):
        # Create a test data file with some content
        with open(self.test_data_file, "w") as file:
            json.dump([{"task": "Test Task", "description": "Test Description", "deadline": "Test Deadline", "completed": False}], file)

        # Test marking a task as complete with mocked input
        mark_task_as_complete()

        # Load data from the test data file
        with open(self.test_data_file, "r") as file:
            data = json.load(file)

        # Check if task is marked as complete correctly
        self.assertTrue(data[0]["completed"])

    @patch('builtins.input', return_value="1")
    def test_delete_task(self, mock_input):
        # Create a test data file with some content
        with open(self.test_data_file, "w") as file:
            json.dump([{"task": "Test Task", "description": "Test Description", "deadline": "Test Deadline", "completed": False}], file)

        # Test deleting a task with mocked input
        delete_task()

        # Load data from the test data file
        with open(self.test_data_file, "r") as file:
            data = json.load(file)

        # Check if task is deleted correctly
        self.assertEqual(data, [])

if __name__ == '__main__':
    unittest.main()