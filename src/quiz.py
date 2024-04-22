import json
import random
from datetime import datetime
from log_manager import LogManager

def add_quiz():
    """
    Adds a new quiz to the quizzes.json file.

    Prompts the user to enter the name of the quiz and a series of questions with their answers.
    The quiz data is then stored in the quizzes.json file.

    Returns:
        None
    """
    quiz = {}
    quiz["name"] = input("Enter the name of the quiz: ")
    quiz["questions"] = []
    while True:
        question = {}
        question["question"] = input("Enter the question: ")
        question["answers"] = []
        while True:
            answer = input("Enter an answer: ")
            question["answers"].append(answer)
            if input("Is this the correct answer? (y/n): ").lower() == "y":
                question["correct_answer"] = answer
            if input("Do you want to add another answer? (y/n): ").lower() == "n":
                break
        quiz["questions"].append(question)
        if input("Do you want to add another question? (y/n): ").lower() == "n":
            break
    with open("files/quizzes.json", "r") as f:
        quizzes = json.load(f)
    quizzes.append(quiz)
    with open("files/quizzes.json", "w") as f:
        json.dump(quizzes, f)
    LogManager.log_activity("Quiz added", "Quiz")

def take_quiz():
    """
    Takes a quiz from the available quizzes and records the user's score in the leaderboard.

    This function prompts the user to choose a quiz from a list of available quizzes,
    displays each question with multiple-choice answers, and records the user's score
    based on their selected answers. The user's name and score are then added to the
    quiz leaderboard.

    Returns:
        None
    """
    with open("files/quizzes.json", "r") as f:
        quizzes = json.load(f)
    print("Choose a quiz to take: ")
    for i, quiz in enumerate(quizzes):
        print(str(i + 1) + ". " + quiz["name"])
    while True:
        try:
            quiz_number = int(input("Enter the number of the quiz you want to take: "))
            if quiz_number in range(1, len(quizzes) + 1):
                break
            else:
                print("Invalid choice. Please enter a number between 1 and " + str(len(quizzes)) + ".")
        except ValueError:
            print("Invalid input. Please enter a number.")
    quiz = quizzes[quiz_number - 1]
    score = 0
    print("Quiz: " + quiz["name"])
    for question in quiz["questions"]:
        print(question["question"])
        for i, answer in enumerate(question["answers"]):
            print(str(i + 1) + ". " + answer)
        while True:
            try:
                user_answer = int(input("Enter the number of your answer: "))
                if user_answer in range(1, len(question["answers"]) + 1):
                    if question["answers"][user_answer - 1] == question["correct_answer"]:
                        score += 1
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and " + str(len(question["answers"])) + ".")
            except ValueError:
                print("Invalid input. Please enter a number.")
    print("Your score is: " + str(score))
    name = input("Enter your name: ")
    with open("files/quiz_leaderboard.json", "r") as f:
        leaderboard = json.load(f)
    leaderboard.append({"name": name, "score": score, "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    with open("files/quiz_leaderboard.json", "w") as f:
        json.dump(leaderboard, f)
    LogManager.log_activity("Quiz taken", "Quiz")

def delete_quiz():
    """
    Deletes a quiz from the quizzes.json file.

    This function prompts the user to select a quiz number to delete from the quizzes.json file.
    It loads the quizzes from the file, displays a list of available quizzes, and asks the user to enter the number of the quiz they want to delete.
    If the input is valid, it removes the selected quiz from the quizzes list, updates the quizzes.json file, and logs the activity.

    Parameters:
    None

    Returns:
    None
    """
    with open("files/quizzes.json", "r") as f:
        quizzes = json.load(f)
    for i, quiz in enumerate(quizzes):
        print(str(i + 1) + ". " + quiz["name"])
    while True:
        try:
            quiz_number = int(input("Enter the number of the quiz you want to delete: "))
            if quiz_number in range(1, len(quizzes) + 1):
                break
            else:
                print("Invalid choice. Please enter a number between 1 and " + str(len(quizzes)) + ".")
        except ValueError:
            print("Invalid input. Please enter a number.")
    del quizzes[quiz_number - 1]
    with open("files/quizzes.json", "w") as f:
        json.dump(quizzes, f)
    LogManager.log_activity("Quiz deleted", "Quiz")

import json

def list_quizzes():
    """
    Lists all the quizzes from the quizzes.json file.
    """
    with open("files/quizzes.json", "r") as f:
        quizzes = json.load(f)
    for quiz in quizzes:
        print("Quiz: " + quiz["name"])
    LogManager.log_activity("Quizzes listed", "Quiz")


