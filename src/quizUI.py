from quiz import add_quiz, take_quiz, delete_quiz, list_quizzes

def run_quizUI():
    """
    Runs the quiz user interface.

    This function displays a menu of options for the user to choose from and
    performs the corresponding actions based on the user's choice.

    Options:
    1. Add a quiz
    2. Take a quiz
    3. Delete a quiz
    4. List all quizzes
    5. Go back

    Returns:
    None
    """
    while True:
        print("1. Add a quiz")
        print("2. Take a quiz")
        print("3. Delete a quiz")
        print("4. List all quizzes")
        print("5. Go back")
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if choice in [1, 2, 3, 4, 5]:
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        if choice == 1:
            add_quiz()
        elif choice == 2:
            take_quiz()
        elif choice == 3:
            delete_quiz()
        elif choice == 4:
            list_quizzes()
        elif choice == 5:
            break
        else:
            print("Invalid choice.")


