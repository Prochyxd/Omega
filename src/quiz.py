import json

class Quiz:
    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, answer):
        self.questions.append((question, answer))

    def take_quiz(self):
        score = 0
        total_questions = len(self.questions)
        for question, answer in self.questions:
            user_answer = input(question + " ")
            if user_answer.lower() == answer.lower():
                score += 1
        print("You scored {} out of {}.".format(score, total_questions))

    def add_more_questions(self):
        num_questions = int(input("Enter the number of additional questions: "))
        for i in range(num_questions):
            question = input("Enter question {}: ".format(len(self.questions) + 1))
            answer = input("Enter the answer: ")
            self.add_question(question, answer)

    def save_to_file(self, filename):
        with open(filename, 'a') as file:
            quiz_data = {
                "name": self.name,
                "questions": self.questions
            }
            json.dump(quiz_data, file)
            file.write('\n')

def load_quizzes_from_file(filename):
    quizzes = []
    with open(filename, 'r') as file:
        for line in file:
            quiz_data = json.loads(line)
            quiz = Quiz(quiz_data["name"])
            quiz.questions = quiz_data["questions"]
            quizzes.append(quiz)
    return quizzes
