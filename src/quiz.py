#quiz.py
#main logic for the program that will work with quizzes from file files/quizzes.json
#user will insert his name to bet displayed in the leaderboard
#user will be able to add quizz with multiple questions and answers
#user will be able to take the quiz and get the score
#user will be able to delete the quiz
#user will be able to list all the quizzes

import json
import random
from datetime import datetime
from log_manager import LogManager

def add_quiz():
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

def list_quizzes():
    with open("files/quizzes.json", "r") as f:
        quizzes = json.load(f)
    for quiz in quizzes:
        print("Quiz: " + quiz["name"])
    LogManager.log_activity("Quizzes listed", "Quiz")


