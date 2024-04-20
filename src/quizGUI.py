import tkinter as tk
from quiz import Quiz, load_quizzes_from_file

class QuizGUI:
    def __init__(self, root, filename):
        self.root = root
        self.root.title("Quiz Application")
        self.filename = filename
        self.quizzes = load_quizzes_from_file(filename)

        self.create_quiz_btn = tk.Button(root, text="Create a Quiz", command=self.create_quiz)
        self.create_quiz_btn.pack()

        self.take_quiz_btn = tk.Button(root, text="Take a Quiz", command=self.take_quiz)
        self.take_quiz_btn.pack()

        self.add_questions_btn = tk.Button(root, text="Add more questions to a Quiz", command=self.add_more_questions)
        self.add_questions_btn.pack()

    def create_quiz(self):
        create_quiz_window = tk.Toplevel(self.root)
        create_quiz_window.title("Create a Quiz")

        quiz_name_label = tk.Label(create_quiz_window, text="Quiz Name:")
        quiz_name_label.grid(row=0, column=0)
        self.quiz_name_entry = tk.Entry(create_quiz_window)
        self.quiz_name_entry.grid(row=0, column=1)

        num_questions_label = tk.Label(create_quiz_window, text="Number of Questions:")
        num_questions_label.grid(row=1, column=0)
        self.num_questions_entry = tk.Entry(create_quiz_window)
        self.num_questions_entry.grid(row=1, column=1)

        submit_btn = tk.Button(create_quiz_window, text="Submit", command=self.submit_quiz)
        submit_btn.grid(row=2, columnspan=2)

    def submit_quiz(self):
        quiz_name = self.quiz_name_entry.get()
        num_questions = int(self.num_questions_entry.get())
        quiz = Quiz(quiz_name)
        for i in range(num_questions):
            question = input("Enter question {}: ".format(i+1))
            answer = input("Enter the answer: ")
            quiz.add_question(question, answer)
        quiz.save_to_file(self.filename)
        print("Quiz created successfully!")

    def take_quiz(self):
        take_quiz_window = tk.Toplevel(self.root)
        take_quiz_window.title("Take a Quiz")

        quiz_name_label = tk.Label(take_quiz_window, text="Quiz Name:")
        quiz_name_label.grid(row=0, column=0)
        self.quiz_name_combobox = tk.StringVar()
        self.quiz_name_combobox.set(list(self.quizzes.keys())[0] if self.quizzes else "")
        quiz_name_dropdown = tk.OptionMenu(take_quiz_window, self.quiz_name_combobox, *self.quizzes.keys())
        quiz_name_dropdown.grid(row=0, column=1)

        take_quiz_btn = tk.Button(take_quiz_window, text="Take Quiz", command=self.take_selected_quiz)
        take_quiz_btn.grid(row=1, columnspan=2)

    def take_selected_quiz(self):
        quiz_name = self.quiz_name_combobox.get()
        for quiz in self.quizzes:
            if quiz.name == quiz_name:
                quiz.take_quiz()
                return
        print("Quiz not found!")

    def add_more_questions(self):
        add_questions_window = tk.Toplevel(self.root)
        add_questions_window.title("Add more questions to a Quiz")

        quiz_name_label = tk.Label(add_questions_window, text="Quiz Name:")
        quiz_name_label.grid(row=0, column=0)
        self.quiz_name_combobox = tk.StringVar()
        self.quiz_name_combobox.set(list(self.quizzes.keys())[0] if self.quizzes else "")
        quiz_name_dropdown = tk.OptionMenu(add_questions_window, self.quiz_name_combobox, *self.quizzes.keys())
        quiz_name_dropdown.grid(row=0, column=1)

        num_questions_label = tk.Label(add_questions_window, text="Number of Additional Questions:")
        num_questions_label.grid(row=1, column=0)
        self.num_questions_entry = tk.Entry(add_questions_window)
        self.num_questions_entry.grid(row=1, column=1)

        submit_btn = tk.Button(add_questions_window, text="Submit", command=self.add_questions_to_quiz)
        submit_btn.grid(row=2, columnspan=2)

    def add_questions_to_quiz(self):
        quiz_name = self.quiz_name_combobox.get()
        num_questions = int(self.num_questions_entry.get())
        for quiz in self.quizzes:
            if quiz.name == quiz_name:
                for i in range(num_questions):
                    question = input("Enter question {}: ".format(len(quiz.questions) + 1))
                    answer = input("Enter the answer: ")
                    quiz.add_question(question, answer)
                quiz.save_to_file(self.filename)
                print("Questions added successfully to the quiz.")
                return
        print("Quiz not found!")

def run_quizGUI():
    root = tk.Tk()
    app = QuizGUI(root, "files/quizzes.json")
    root.mainloop()
