# math_tests.py

import random
import time
import json

def load_problems():
    with open("files/math_problems.json", "r", encoding="utf-8") as file:
        problems = json.load(file)
    return problems

def choose_problems(problems):
    print("Choose a math category:")
    print("1. Addition and Subtraction")
    print("2. Multiplication and Division")
    print("3. Quadratic Equations")
    print("4. Other")
    choice = input("Enter choice: ")
    if choice == "1":
        return problems["addition_subtraction"]
    elif choice == "2":
        return problems["multiplication_division"]
    elif choice == "3":
        return problems["quadratic_equations"]
    elif choice == "4":
        return problems["other"]
    else:
        print("Invalid choice. Please try again.")
        return choose_problems(problems)
    
def choose_difficulty(problems):
    print("Choose a difficulty:")
    print("1. Easy")
    print("2. Hard")
    choice = input("Enter choice: ")
    if choice == "1":
        return problems["easy"]
    elif choice == "2":
        return problems["hard"]
    else:
        print("Invalid choice. Please try again.")
        return choose_difficulty(problems)
    
def get_problem(problems):
    problem = random.choice(problems)
    return problem

def get_score(problems):
    score = 0
    for problem in problems:
        print("--------------------")
        print("Math problem: " + problem["problem"])
        for i, choice in enumerate(problem["choices"]):
            print(f"{i + 1}. {choice}")
        answer = input("Enter answer (the number you calculated): ")
        if answer == problem["answer"]:
            score += 1
    return score

def save_score(name, score, time_taken):
    with open("files/math_problems_leaderboard.json", "r", encoding="utf-8") as file:
        leaderboard = json.load(file)
    leaderboard.append({"name": name, "score": score, "time_taken": time_taken})
    leaderboard = sorted(leaderboard, key=lambda x: x["score"], reverse=True)
    with open("files/math_problems_leaderboard.json", "w", encoding="utf-8") as file:
        json.dump(leaderboard, file, indent=4)
