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


def math_tests():
    print("Welcome to Math Tests!")
    print("(Little advice: For harder math problems i reccoment to copy and paste one of given choises (this progam is not case sensitive))")
    print("Enter your name that will be used for the leaderboard:")
    name = input("Enter name: ")
    print(f"Hello, {name}!")

    problems = load_problems()
    category = choose_problems(problems)
    difficulty = choose_difficulty(category)
    problems = [get_problem(difficulty) for _ in range(10)]
    start_time = time.time()
    score = get_score(problems)
    end_time = time.time()
    time_taken = end_time - start_time
    print(f"Score: {score}")
    print(f"Time taken: {time_taken:.2f} seconds")
    save_score(name, score, time_taken)
    print("Leaderboard:")
    with open("files/math_problems_leaderboard.json", "r", encoding="utf-8") as file:
        leaderboard = json.load(file)
    for i, player in enumerate(leaderboard):
        print(f"{i + 1}. {player['name']} - {player['score']} - {player['time_taken']:.2f} seconds")


