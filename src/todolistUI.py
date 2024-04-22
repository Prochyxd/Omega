import todolist

def add_task():
    """
    Adds a task to the to-do list.

    Prompts the user to enter the task, description, and deadline (optional).
    Calls the `add_task` method of the `todolist` object to add the task.
    Prints a success message after adding the task.
    """
    task = input("Enter the task: ")
    description = input("Enter the task description (optional): ")
    deadline = input("Enter the deadline of your task (optional): ")
    todolist.add_task(task, description, deadline)
    print("Task added successfully.")

def view_all_tasks():
    """
    View all tasks in the to-do list.

    This function retrieves all tasks from the to-do list and displays them in the console.
    If there are no tasks, it prints a message indicating that no tasks were found.

    Parameters:
    None

    Returns:
    None
    """
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
    """
    Marks a task as complete in the todo list.

    Prompts the user to enter the task number to mark as complete.
    If the task number is valid, it marks the task as complete and returns True.
    If the task number is invalid, it returns False.

    Returns:
        bool: True if the task was marked as complete, False otherwise.
    """
    task_number = get_valid_task_number("Enter the task number to mark as complete: ")
    if todolist.mark_task_as_complete(task_number):
        print("Task marked as complete.")
        return True
    else:
        print("Invalid task number.")
        return False

def delete_task():
    """
    Deletes a task from the todo list.

    Prompts the user to enter the task number to delete.
    If the task number is valid and the task is successfully deleted,
    it prints "Task deleted successfully". Otherwise, it prints "Invalid task number".
    """
    task_number = get_valid_task_number("Enter the task number to delete: ")
    if todolist.delete_task(task_number):
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

def get_valid_task_number(prompt):
    """
    Prompts the user to enter a valid task number.

    Args:
        prompt (str): The prompt to display to the user.

    Returns:
        int: The valid task number entered by the user.

    Raises:
        ValueError: If the user enters an invalid task number.

    """
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
    """
    Main function for the to-do list application.
    Displays a menu of options and performs the corresponding actions based on user input.
    """
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
