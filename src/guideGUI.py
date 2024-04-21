import tkinter as tk
from tkinter import messagebox

def overall_guide():
    messagebox.showinfo("Overall Guide",
                        "This program is a collection of different applications.\n"
                        "There are five applications in this program:\n"
                        "1. Math tests\n"
                        "2. To-Do List\n"
                        "3. Compression\n"
                        "4. Quiz\n"
                        "5. Work with txt\n"
                        "You can choose the interface you want to use for each application (Console UI or GUI).\n"
                        "Enjoy using the program!")

def math_tests_guide():
    messagebox.showinfo("Math Tests Guide",
                        "This application is a collection of math tests.\n"
                        "You can choose the branch and difficulty of the tests.\n"
                        "You can also choose the interface you want to use (Console UI or GUI).\n"
                        "Step by step: choose the branch, choose the difficulty, answer the questions, and see your score.")

def todo_list_guide():
    messagebox.showinfo("To-Do List Guide",
                        "This application is a simple To-Do List.\n"
                        "You can add tasks, mark them as done, and delete them.\n"
                        "You can also choose the interface you want to use (Console UI or GUI).\n"
                        "Step by step: add a task, mark it as done, delete it.")

def compression_guide():
    messagebox.showinfo("Compression Guide",
                        "This application is a compression program.\n"
                        "You can also choose the interface you want to use (Console UI or GUI).\n"
                        "Step by step: choose the file you want to compress, choose the words in the file you want to change, then write the short form of it and compress the file.")

def quiz_guide():
    messagebox.showinfo("Quiz Guide",
                        "This application is a quiz application.\n"
                        "You can make quizzes, take part in them, or delete them.\n"
                        "You can also choose the interface you want to use (Console UI or GUI).\n"
                        "Step by step: make a quiz, take part in it, see the leaderboard.")

def work_with_txt_guide():
    messagebox.showinfo("Work with txt Guide",
                        "This application is a program that allows you to work with txt files.\n"
                        "You can read, write, copy, delete, rename, and many other functions with the text files.\n"
                        "You can also choose the interface you want to use (Console UI or GUI).\n"
                        "Step by step: choose the file you want to work with, choose the function you want to use, then do the function.")

def run_guide_gui():
    root = tk.Tk()
    root.title("Guide UI")

    label = tk.Label(root, text="Do you want to see the overall guide of the program or the guide of a specific part of the program?")
    label.pack()

    overall_button = tk.Button(root, text="Overall Guide", command=overall_guide)
    overall_button.pack()

    specific_button = tk.Button(root, text="Specific Guide", command=lambda: specific_guide(root))
    specific_button.pack()

    exit_button = tk.Button(root, text="Exit", command=root.destroy)
    exit_button.pack()

    root.mainloop()

def specific_guide(root):
    specific_guide_window = tk.Toplevel(root)
    specific_guide_window.title("Specific Guide")

    label = tk.Label(specific_guide_window, text="Which part of the program do you want to see the guide of?")
    label.pack()

    math_tests_button = tk.Button(specific_guide_window, text="Math Tests", command=math_tests_guide)
    math_tests_button.pack()

    todo_list_button = tk.Button(specific_guide_window, text="To-Do List", command=todo_list_guide)
    todo_list_button.pack()

    compression_button = tk.Button(specific_guide_window, text="Compression", command=compression_guide)
    compression_button.pack()

    quiz_button = tk.Button(specific_guide_window, text="Quiz", command=quiz_guide)
    quiz_button.pack()

    work_with_txt_button = tk.Button(specific_guide_window, text="Work with txt", command=work_with_txt_guide)
    work_with_txt_button.pack()

