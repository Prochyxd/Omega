import json
import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime
from log_manager import LogManager  # Assuming you have this module


class QuizGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Application")

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.button_add = tk.Button(self.frame, text="Add a quiz", command=self.add_quiz)
        self.button_add.pack()

        self.button_take = tk.Button(self.frame, text="Take a quiz", command=self.take_quiz)
        self.button_take.pack()

        self.button_delete = tk.Button(self.frame, text="Delete a quiz", command=self.delete_quiz)
        self.button_delete.pack()

        self.button_list = tk.Button(self.frame, text="List all quizzes", command=self.list_quizzes)
        self.button_list.pack()

        self.button_leaderboard = tk.Button(self.frame, text="Show leaderboard", command=self.show_leaderboard)
        self.button_leaderboard.pack()

        self.button_quit = tk.Button(self.frame, text="Quit", command=self.master.quit)
        self.button_quit.pack()

    def add_quiz(self):
        name = simpledialog.askstring("Add Quiz", "Enter the name of the quiz:")
        if name:
            quiz = {"name": name, "questions": []}
            while True:
                question_text = simpledialog.askstring("Add Quiz", "Enter the question:")
                if not question_text:
                    break
                answers = []
                while True:
                    answer = simpledialog.askstring("Add Quiz", "Enter an answer:")
                    if not answer:
                        break
                    answers.append(answer)
                    is_correct = messagebox.askyesno("Add Quiz", "Is this the correct answer?")
                    if is_correct:
                        correct_answer = answer
                quiz["questions"].append({"question": question_text, "answers": answers, "correct_answer": correct_answer})
            self.save_quiz(quiz)
            LogManager.log_activity("Quiz added", "Quiz")

    def save_quiz(self, quiz):
        with open("files/quizzes.json", "r") as f:
            quizzes = json.load(f)
        quizzes.append(quiz)
        with open("files/quizzes.json", "w") as f:
            json.dump(quizzes, f)

    def take_quiz(self):
        with open("files/quizzes.json", "r") as f:
            quizzes = json.load(f)
        quiz_names = [quiz["name"] for quiz in quizzes]
        if not quiz_names:
            messagebox.showinfo("Take Quiz", "No quizzes available.")
            return

        selected_quiz = simpledialog.askstring("Take Quiz", "Enter the name of the quiz you want to take:")
        if selected_quiz:
            for quiz in quizzes:
                if quiz["name"].lower() == selected_quiz.lower():
                    score = 0
                    for question in quiz["questions"]:
                        user_answer = simpledialog.askstring("Take Quiz", question["question"] + "\n" + "\n".join(question["answers"]))
                        if user_answer == question["correct_answer"]:
                            score += 1
                    name = simpledialog.askstring("Take Quiz", "Enter your name:")
                    with open("files/quiz_leaderboard.json", "r") as f:
                        leaderboard = json.load(f)
                    leaderboard.append({"name": name, "score": score, "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
                    with open("files/quiz_leaderboard.json", "w") as f:
                        json.dump(leaderboard, f)
                    LogManager.log_activity("Quiz taken", "Quiz")
                    messagebox.showinfo("Quiz Results", "Your score is: {}".format(score))
                    return
            messagebox.showinfo("Take Quiz", "Quiz not found.")

    def delete_quiz(self):
        with open("files/quizzes.json", "r") as f:
            quizzes = json.load(f)
        quiz_names = [quiz["name"] for quiz in quizzes]
        if not quiz_names:
            messagebox.showinfo("Delete Quiz", "No quizzes available.")
            return

        selected_quiz = simpledialog.askstring("Delete Quiz", "Enter the name of the quiz you want to delete:")
        if selected_quiz:
            for quiz in quizzes:
                if quiz["name"].lower() == selected_quiz.lower():
                    quizzes.remove(quiz)
                    with open("files/quizzes.json", "w") as f:
                        json.dump(quizzes, f)
                    LogManager.log_activity("Quiz deleted", "Quiz")
                    messagebox.showinfo("Delete Quiz", "Quiz deleted successfully.")
                    return
            messagebox.showinfo("Delete Quiz", "Quiz not found.")

    def list_quizzes(self):
        with open("files/quizzes.json", "r") as f:
            quizzes = json.load(f)
        quiz_names = [quiz["name"] for quiz in quizzes]
        if not quiz_names:
            messagebox.showinfo("List Quizzes", "No quizzes available.")
            return

        messagebox.showinfo("List Quizzes", "\n".join(quiz_names))
        LogManager.log_activity("Quizzes listed", "Quiz")

    def show_leaderboard(self):
        with open("files/quiz_leaderboard.json", "r") as f:
            leaderboard = json.load(f)
        leaderboard_info = ["Name: {}, Score: {}, Date: {}".format(entry["name"], entry["score"], entry["date"]) for entry in leaderboard]
        if not leaderboard_info:
            messagebox.showinfo("Leaderboard", "No entries in the leaderboard.")
            return

        messagebox.showinfo("Leaderboard", "\n".join(leaderboard_info))
        LogManager.log_activity("Leaderboard shown", "Quiz")


def run_quiz_GUI():
    root = tk.Tk()
    app = QuizGUI(root)
    root.mainloop()

