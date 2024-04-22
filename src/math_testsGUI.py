import tkinter as tk
import math_tests as math_tests_module
import random
import time
import json

class MathTestsGUI:
    def __init__(self, root):
        """
        Initialize the MathTestsGUI class.

        Args:
            root: The root Tkinter window.

        Attributes:
            root (Tk): The root Tkinter window.
            problems (list): A list of math problems.
            name_label (Label): The label for entering the name.
            name_entry (Entry): The entry field for entering the name.
            start_button (Button): The button for starting the math tests.
            category_label (Label): The label for selecting the category.
            difficulty_label (Label): The label for selecting the difficulty.
            category_radio_buttons (list): A list of radio buttons for selecting the category.
            difficulty_radio_buttons (list): A list of radio buttons for selecting the difficulty.
            answer_entry (Entry): The entry field for entering the answer.
        """
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

        self.answer_entry = None

    def start_tests(self):
        """
        Starts the math tests.

        This method retrieves the player's name from the name_entry widget.
        If the name is not provided, it displays an error message.
        Otherwise, it sets the player_name attribute and proceeds to create the GUI for selecting math category and difficulty.
        """
        name = self.name_entry.get().strip()
        if not name:
            tk.messagebox.showerror("Error", "Please enter your name.")
            return

        self.player_name = name 

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
            """
            Starts the math tests by performing the following steps:
            1. Destroys the category label, difficulty label, and start tests button.
            2. Disables all category and difficulty radio buttons.
            3. Retrieves the selected category and difficulty.
            4. Retrieves a list of problems based on the selected category and difficulty.
            5. Shuffles the list of problems.
            6. Selects the first 10 problems from the shuffled list.
            7. Creates and displays the score label.
            8. Creates and displays the score display label.
            9. Records the start time of the tests.
            10. Sets the current problem index to 0.
            11. Calls the show_problem method to display the first problem from the list.

            Parameters:
            - None

            Returns:
            - None
            """
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
        """
        Displays a problem from the given list of problems.

        Parameters:
        - problems (list): A list of dictionaries representing the problems. Each dictionary should have a "problem" key.

        Returns:
        None
        """
        if self.current_problem_index >= len(problems):
            self.end_tests()
            return

        problem = problems[self.current_problem_index]

        self.problem_label = tk.Label(self.root, text=problem["problem"])
        self.problem_label.pack()

        self.answer_entry = tk.Entry(self.root)
        self.answer_entry.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        self.submit_button.pack()

    def check_answer(self):
            """
            Checks the user's answer and updates the score.

            Retrieves the user's answer from the answer_entry widget and strips any leading or trailing whitespace.
            Retrieves the current problem based on the selected category, difficulty, and current problem index.
            If the user's answer is empty, displays an error message and returns.
            If the user's answer matches the correct answer for the problem, increments the score by 1.
            Destroys the problem_label, answer_entry, and submit_button widgets.
            Increments the current_problem_index by 1.
            Calls the show_problem method to display the next problem.

            Returns:
                None
            """
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
        """
        Ends the math tests and saves the score to the leaderboard.

        Calculates the time taken for the tests, saves the score to the leaderboard file,
        and destroys the score label, problem label, and submit button. Then, it displays
        the leaderboard on the GUI.

        Returns:
            None
        """
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
