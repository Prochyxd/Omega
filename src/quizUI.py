from quiz import Quiz, load_quizzes_from_file

class QuizUI:
    def __init__(self, filename):
        self.filename = filename
        self.quizzes = load_quizzes_from_file(filename)

    def create_quiz(self):
        quiz_name = input("Enter the name of the quiz: ")
        quiz = Quiz(quiz_name)
        num_questions = int(input("Enter the number of questions: "))
        for i in range(num_questions):
            question = input("Enter question {}: ".format(i+1))
            answer = input("Enter the answer: ")
            quiz.add_question(question, answer)
        quiz.save_to_file(self.filename)
        print("Quiz created successfully!")

    def take_quiz(self):
        quiz_name = input("Enter the name of the quiz you want to take: ")
        for quiz in self.quizzes:
            if quiz.name == quiz_name:
                quiz.take_quiz()
                return
        print("Quiz not found!")

    def add_more_questions(self):
        quiz_name = input("Enter the name of the quiz you want to add more questions to: ")
        for quiz in self.quizzes:
            if quiz.name == quiz_name:
                quiz.add_more_questions()
                quiz.save_to_file(self.filename)
                print("Questions added successfully to the quiz.")
                return
        print("Quiz not found!")

def run_quizUI():
    ui = QuizUI("files/quizzes.json")
    while True:
        print("1. Create a Quiz")
        print("2. Take a Quiz")
        print("3. Add more questions to a Quiz")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            ui.create_quiz()

        elif choice == "2":
            ui.take_quiz()

        elif choice == "3":
            ui.add_more_questions()

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")
