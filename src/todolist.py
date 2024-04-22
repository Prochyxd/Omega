import json
import os
from log_manager import LogManager

def load_data():
    """
    Load data from the 'tododata.json' file.

    If the file exists, it is opened and its contents are loaded as JSON data.
    If the file does not exist, an empty list is returned.

    Returns:
        list: The loaded data from the 'tododata.json' file, or an empty list if the file does not exist.
    """
    if os.path.exists("files/tododata.json"):
        with open("files/tododata.json", "r") as file:
            data = json.load(file)
        return data
    else:
        return []

def save_data(data):
    """
    Save the given data to a JSON file.

    Args:
        data (dict): The data to be saved.

    Returns:
        None
    """
    with open("files/tododata.json", "w") as file:
        json.dump(data, file)

def add_task(task, description, deadline):
    """
    Add a new task to the to-do list.

    Args:
        task (str): The name of the task.
        description (str): A description of the task.
        deadline (str): The deadline for completing the task.

    Returns:
        None
    """
    data = load_data()
    data.append({"task": task, "description": description, "deadline": deadline, "completed": False})
    save_data(data)
    LogManager.log_activity("Task Added", f"Task: {task}, Description: {description}, Deadline: {deadline}")

def view_all_tasks():
    """
    Retrieves and returns all tasks from the data source.

    Returns:
        list: A list of all tasks.
    """
    data = load_data()
    return data

def mark_task_as_complete(task_number):
    """
    Marks a task as complete based on the given task number.

    Args:
        task_number (int): The number of the task to mark as complete.

    Returns:
        bool: True if the task was successfully marked as complete, False otherwise.
    """
    try:
        task_number = int(task_number)
        data = load_data()
        if 1 <= task_number <= len(data):
            data[task_number - 1]["completed"] = True
            save_data(data)
            LogManager.log_activity("Task Marked as Complete", f"Task number: {task_number}")
            return True
        else:
            return False
    except ValueError:
        return False
    
def delete_task(task_number):
    """
    Delete a task from the to-do list.

    Args:
        task_number (int): The number of the task to be deleted.

    Returns:
        bool: True if the task was successfully deleted, False otherwise.
    """
    try:
        task_number = int(task_number)
        data = load_data()
        if 1 <= task_number <= len(data):
            del data[task_number - 1]
            save_data(data)
            LogManager.log_activity("Task Deleted", f"Task number: {task_number}")
            return True
        else:
            return False
    except ValueError:
        return False
