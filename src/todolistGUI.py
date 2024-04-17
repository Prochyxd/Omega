# todolistGUI.py

import tkinter as tk
import todolist

def add_task():
    task = task_entry.get()
    description = description_entry.get()
    deadline = deadline_entry.get()
    
    todolist.add_task(task, description, deadline)
    result_label.config(text="Task added successfully.")

def view_all_tasks():
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
    task_number = int(mark_task_entry.get())
    if todolist.mark_task_as_complete(task_number):
        result_label.config(text="Task marked as complete.")
    else:
        result_label.config(text="Invalid task number.")

def delete_task():
    task_number = int(delete_task_entry.get())
    if todolist.delete_task(task_number):
        result_label.config(text="Task deleted successfully.")
    else:
        result_label.config(text="Invalid task number.")

root = tk.Tk()
root.title("To-Do List")

# Add Task Section
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

# View Tasks Section
view_frame = tk.Frame(root)
view_frame.pack(pady=10)

view_button = tk.Button(view_frame, text="View All Tasks", command=view_all_tasks)
view_button.pack()

tasks_text = tk.Text(view_frame, height=10, width=50)
tasks_text.pack()

# Mark Task as Complete Section
mark_frame = tk.Frame(root)
mark_frame.pack(pady=10)

tk.Label(mark_frame, text="Task Number:").grid(row=0, column=0)
mark_task_entry = tk.Entry(mark_frame)
mark_task_entry.grid(row=0, column=1)

mark_button = tk.Button(mark_frame, text="Mark Task as Complete", command=mark_task_as_complete)
mark_button.grid(row=1, columnspan=2)

# Delete Task Section
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
