import tkinter as tk
import todolist

def add_task():
    """
    Adds a task to the to-do list.

    Retrieves the task, description, and deadline from the corresponding entry fields.
    If both the task and deadline are provided, the task is added to the to-do list
    using the `add_task` method of the `todolist` object. The result label is updated
    accordingly.

    If either the task or deadline is missing, an error message is displayed.

    Parameters:
        None

    Returns:
        None
    """
    task = task_entry.get()
    description = description_entry.get()
    deadline = deadline_entry.get()
    
    if task and deadline:
        todolist.add_task(task, description, deadline)
        result_label.config(text="Task added successfully.")
    else:
        result_label.config(text="Please enter a task and deadline.")

def view_all_tasks():
    """
    Displays all tasks in the tasks_text widget.

    Retrieves all tasks from the todolist and displays them in the tasks_text widget.
    If there are no tasks, it displays a message indicating that no tasks were found.
    Each task is displayed with its index, task name, status, description (if available),
    and deadline (if available).
    """
    tasks_text.delete("1.0", tk.END)
    tasks = todolist.view_all_tasks()
    if tasks:
        tasks_text.insert(tk.END, "All tasks:\n")
        for i, task in enumerate(tasks, 1):
            status = "Completed" if task["completed"] else "Not Completed"
            description = task["description"]
            deadline = task["deadline"]
            tasks_text.insert(tk.END, f"{i}. {task['task']} - {status}\n")
            if description:
                tasks_text.insert(tk.END, f"   Description: {description}\n")
            if deadline:
                tasks_text.insert(tk.END, f"   Deadline: {task['deadline']}\n")
    else:
        tasks_text.insert(tk.END, "No tasks found.")

def mark_task_as_complete():
    """
    Marks a task as complete based on the task number entered by the user.

    The function attempts to convert the input from the `mark_task_entry` widget into an integer.
    If successful, it calls the `mark_task_as_complete` method of the `todolist` object with the task number.
    If the task is successfully marked as complete, it updates the `result_label` widget with the message "Task marked as complete."
    If the task number is invalid, it updates the `result_label` widget with the message "Invalid task number."
    If the input cannot be converted to an integer, it updates the `result_label` widget with the message "Please enter a valid task number."
    """
    try:
        task_number = int(mark_task_entry.get())
        if todolist.mark_task_as_complete(task_number):
            result_label.config(text="Task marked as complete.")
        else:
            result_label.config(text="Invalid task number.")
    except ValueError:
        result_label.config(text="Please enter a valid task number.")

def delete_task():
    """
    Deletes a task from the to-do list.

    This function takes the task number entered in the delete_task_entry widget,
    converts it to an integer, and attempts to delete the corresponding task
    from the to-do list. If the task is successfully deleted, it updates the
    result_label widget with a success message. If the task number is invalid,
    it updates the result_label widget with an error message. If the task number
    is not a valid integer, it updates the result_label widget with a validation
    error message.

    Parameters:
    None

    Returns:
    None
    """
    try:
        task_number = int(delete_task_entry.get())
        if todolist.delete_task(task_number):
            result_label.config(text="Task deleted successfully.")
        else:
            result_label.config(text="Invalid task number.")
    except ValueError:
        result_label.config(text="Please enter a valid task number.")

root = tk.Tk()
root.title("To-Do List")

add_frame = tk.Frame(root)
add_frame.pack(pady=10)

tk.Label(add_frame, text="Task:").grid(row=0, column=0)

task_entry = tk.Entry(add_frame)
task_entry.grid(row=0, column=1)

tk.Label(add_frame, text="Description:").grid(row=1, column=0)

description_entry = tk.Entry(add_frame)
description_entry.grid(row=1, column=1)

tk.Label(add_frame, text="Deadline:").grid(row=2, column=0)

deadline_entry = tk.Entry(add_frame)
deadline_entry.grid(row=2, column=1)

add_button = tk.Button(add_frame, text="Add Task", command=add_task)
add_button.grid(row=3, columnspan=2)


view_frame = tk.Frame(root)
view_frame.pack(pady=10)
view_button = tk.Button(view_frame, text="View All Tasks", command=view_all_tasks)
view_button.pack()
tasks_text = tk.Text(view_frame, height=10, width=50)
tasks_text.pack()


mark_frame = tk.Frame(root)
mark_frame.pack(pady=10)
tk.Label(mark_frame, text="Task Number:").grid(row=0, column=0)
mark_task_entry = tk.Entry(mark_frame)
mark_task_entry.grid(row=0, column=1)
mark_button = tk.Button(mark_frame, text="Mark Task as Complete", command=mark_task_as_complete)
mark_button.grid(row=1, columnspan=2)


delete_frame = tk.Frame(root)
delete_frame.pack(pady=10)
tk.Label(delete_frame, text="Task Number:").grid(row=0, column=0)
delete_task_entry = tk.Entry(delete_frame)
delete_task_entry.grid(row=0, column=1)
delete_button = tk.Button(delete_frame, text="Delete Task", command=delete_task)
delete_button.grid(row=1, columnspan=2)
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
