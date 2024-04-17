# math_testsUI.py

import json
import time
import math_tests

def math_tests():
    print("Welcome to Math Tests!")
    print("(Little advice: For harder math problems i reccoment to copy and paste one of given choises (this progam is not case sensitive))")
    print("Enter your name that will be used for the leaderboard:")
    name = input("Enter name: ")
    print(f"Hello, {name}!")

    problems = math_tests.load_problems()
    category = math_tests.choose_problems(problems)
    difficulty = math_tests.choose_difficulty(category)
    problems = [math_tests.get_problem(difficulty) for _ in range(10)]
    start_time = time.time()
    score = math_tests.get_score(problems)
    end_time = time.time()
    time_taken = end_time - start_time
    print(f"Score: {score}")
    print(f"Time taken: {time_taken:.2f} seconds")
    math_tests.save_score(name, score, time_taken)
    print("Leaderboard:")
    with open("files/math_problems_leaderboard.json", "r", encoding="utf-8") as file:
        leaderboard = json.load(file)
    for i, player in enumerate(leaderboard):
        print(f"{i + 1}. {player['name']} - {player['score']} - {player['time_taken']:.2f} seconds")
