#This will be program to make my own to do list
#it will load and save data to a json file files\tododata.json
#it will have the following options
#1. Add a task
#2. View all tasks
#3. Mark task as complete
#4. Delete a task
#5. Exit

import json
import os

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

def add_task():
    data = load_data()
    task = input("Enter the task: ")
    description = input("Enter the task description (optional): ")
    data.append({"task": task, "description": description, "completed": False})
    save_data(data)
    print("Task added successfully.")

def view_all_tasks():
    data = load_data()
    if data:
        print("All tasks:")
        for i, task in enumerate(data, 1):
            status = "Completed" if task["completed"] else "Not Completed"
            description = task["description"]
            print(f"{i}. {task['task']} - {status}")
            if description:
                print(f"   Description: {description}")
    else:
        print("No tasks found.")

def mark_task_as_complete():
    data = load_data()
    view_all_tasks()
    task_number = int(input("Enter the task number to mark as complete: "))
    if 1 <= task_number <= len(data):
        data[task_number - 1]["completed"] = True
        save_data(data)
        print("Task marked as complete.")
    else:
        print("Invalid task number.")

def delete_task():
    data = load_data()
    view_all_tasks()
    task_number = int(input("Enter the task number to delete: "))
    if 1 <= task_number <= len(data):
        del data[task_number - 1]
        save_data(data)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

def todo():
    while True:
        print("\nChoose an option:")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Mark task as complete")
        print("4. Delete a task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_all_tasks()
        elif choice == "3":
            mark_task_as_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

            