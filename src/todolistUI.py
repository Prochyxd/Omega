import todolist

# todolistUI.py


def add_task():
    task = input("Enter the task: ")
    description = input("Enter the task description (optional): ")
    deadline = input("Enter the deadline of your task (optional): ")
    todolist.add_task(task, description, deadline)
    print("Task added successfully.")

def view_all_tasks():
    tasks = todolist.view_all_tasks()
    if tasks:
        print("All tasks:")
        for i, task in enumerate(tasks, 1):
            status = "Completed" if task["completed"] else "Not Completed"
            description = task["description"]
            deadline = task["deadline"]
            print(f"{i}. {task['task']} - {status}")
            if description:
                print(f"   Description: {description}")
            if deadline:
                print(f"   Deadline: {task['deadline']}")
    else:
        print("No tasks found.")

def mark_task_as_complete():
    task_number = get_valid_task_number("Enter the task number to mark as complete: ")
    if todolist.mark_task_as_complete(task_number):
        print("Task marked as complete.")
    else:
        print("Invalid task number.")

def delete_task():
    task_number = get_valid_task_number("Enter the task number to delete: ")
    if todolist.delete_task(task_number):
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

def get_valid_task_number(prompt):
    while True:
        try:
            task_number = int(input(prompt))
            if task_number > 0:
                return task_number
            else:
                print("Invalid task number. Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")

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
