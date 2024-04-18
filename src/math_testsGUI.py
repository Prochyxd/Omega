import tkinter as tk
import math_tests as math_tests_module
import random
import time
import json

class MathTestsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Tests")
        self.root.geometry("800x600")  # Set the size of the window

        self.problems = math_tests_module.load_problems()

        self.name_label = tk.Label(root, text="Enter your name:")
        self.name_label.pack()

        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.start_button = tk.Button(root, text="Start Math Tests", command=self.start_tests)
        self.start_button.pack()

        self.category_label = None
        self.difficulty_label = None
        self.category_radio_buttons = []
        self.difficulty_radio_buttons = []

        # Define answer entry
        self.answer_entry = None

    def start_tests(self):
        name = self.name_entry.get().strip()
        if not name:
            tk.messagebox.showerror("Error", "Please enter your name.")
            return

        self.player_name = name  # Save the name

        self.name_label.destroy()
        self.name_entry.destroy()
        self.start_button.destroy()

        self.category_label = tk.Label(self.root, text="Choose a math category:")
        self.category_label.pack()

        self.category_var = tk.StringVar()
        self.category_var.set("addition_subtraction")

        categories = [("Addition and Subtraction", "addition_subtraction"),
                      ("Multiplication and Division", "multiplication_division"),
                      ("Quadratic Equations", "quadratic_equations"),
                      ("Other", "other")]

        for text, category in categories:
            radio_button = tk.Radiobutton(self.root, text=text, variable=self.category_var, value=category)
            radio_button.pack()
            self.category_radio_buttons.append(radio_button)

        self.difficulty_label = tk.Label(self.root, text="Choose a difficulty:")
        self.difficulty_label.pack()

        self.difficulty_var = tk.StringVar()
        self.difficulty_var.set("easy")

        difficulty_options = [("Easy", "easy"), ("Hard", "hard")]
        for text, value in difficulty_options:
            radio_button = tk.Radiobutton(self.root, text=text, variable=self.difficulty_var, value=value)
            radio_button.pack()
            self.difficulty_radio_buttons.append(radio_button)

        self.start_tests_button = tk.Button(self.root, text="Start Tests", command=self.start_math_tests)
        self.start_tests_button.pack()

    def start_math_tests(self):
        for widget in [self.category_label, self.difficulty_label, self.start_tests_button]:
            widget.destroy()
        for radio_button in self.category_radio_buttons + self.difficulty_radio_buttons:
            radio_button.configure(state="disabled")

        category = self.category_var.get()
        difficulty = self.difficulty_var.get()
        problems = self.problems[category][difficulty]
        random.shuffle(problems)
        problems = problems[:10]

        self.score_label = tk.Label(self.root, text="Score:")
        self.score_label.pack()

        self.score_var = tk.StringVar()
        self.score_var.set("0")
        score_display = tk.Label(self.root, textvariable=self.score_var)
        score_display.pack()

        self.start_time = time.time()

        self.current_problem_index = 0
        self.show_problem(problems)

    def show_problem(self, problems):
        if self.current_problem_index >= len(problems):
            self.end_tests()
            return

        problem = problems[self.current_problem_index]

        self.problem_label = tk.Label(self.root, text=problem["problem"])
        self.problem_label.pack()

        # Entry for user's answer
        self.answer_entry = tk.Entry(self.root)
        self.answer_entry.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        self.submit_button.pack()

    def check_answer(self):
        user_answer = self.answer_entry.get().strip()
        problem = self.problems[self.category_var.get()][self.difficulty_var.get()][self.current_problem_index]

        if not user_answer:
            tk.messagebox.showerror("Error", "Please enter your answer.")
            return

        if user_answer == problem["answer"]:
            self.score_var.set(int(self.score_var.get()) + 1)

        self.problem_label.destroy()
        self.answer_entry.destroy()
        self.submit_button.destroy()

        self.current_problem_index += 1
        self.show_problem(self.problems[self.category_var.get()][self.difficulty_var.get()])

    def end_tests(self):
        end_time = time.time()
        time_taken = end_time - self.start_time

        math_tests_module.save_score(self.player_name, int(self.score_var.get()), time_taken)

        self.score_label.destroy()
        self.problem_label.destroy()
        self.submit_button.destroy()

        self.leaderboard_label = tk.Label(self.root, text="Leaderboard:")
        self.leaderboard_label.pack()

        with open("files/math_problems_leaderboard.json", "r", encoding="utf-8") as file:
            leaderboard = json.load(file)
            leaderboard = sorted(leaderboard, key=lambda x: (x["score"], -x["time_taken"]), reverse=True)

            for i, player in enumerate(leaderboard, 1):
                tk.Label(self.root, text=f"{i}. {player['name']} - {player['score']} - {player['time_taken']:.2f} seconds").pack()


def math_tests_gui():
    root = tk.Tk()
    app = MathTestsGUI(root)
    root.mainloop()