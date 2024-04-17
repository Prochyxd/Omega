# todolist.py

import json
import os
from log_manager import LogManager

def load_data():
    if os.path.exists("files/tododata.json"):
        with open("files/tododata.json", "r") as file:
            data = json.load(file)
        return data
    else:
        return []

def save_data(data):
    with open("files/tododata.json", "w") as file:
        json.dump(data, file)

def add_task(task, description="", deadline=""):
    data = load_data()
    data.append({"task": task, "description": description, "deadline": deadline, "completed": False})
    save_data(data)
    LogManager.log_activity("Task Added", f"Task: {task}, Description: {description}, Deadline: {deadline}")

def view_all_tasks():
    data = load_data()
    return data

def mark_task_as_complete(task_number):
    data = load_data()
    if 1 <= task_number <= len(data):
        data[task_number - 1]["completed"] = True
        save_data(data)
        LogManager.log_activity("Task Marked as Complete", f"Task number: {task_number}")
        return True
    else:
        return False

def delete_task(task_number):
    data = load_data()
    if 1 <= task_number <= len(data):
        del data[task_number - 1]
        save_data(data)
        LogManager.log_activity("Task Deleted", f"Task number: {task_number}")
        return True
    else:
        return False
