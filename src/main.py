from log_manager import LogManager
from log_managerGUI import run_log_manager_gui
from compressionUI import compression
from compressionGUI import run_compression_gui
import math_testsUI
import math_testsGUI
import todolistUI
from authUI import run_auth_ui
from authGUI import run_auth_gui
from quizGUI import run_quiz_GUI
from quizUI import run_quizUI
from work_with_txtUI import work_with_txt
from work_with_txtGUI import run_work_with_txtGUI



def choose_math_tests_interface():
    print("Welcome to Math Tests!")
    print("Choose the interface you want to use:")
    print("1. Console UI")
    print("2. GUI")
    while True:
        try:
            MathTestsUIchoice = int(input("Enter your choice (1 or 2): "))
            if MathTestsUIchoice in [1, 2]:
                return MathTestsUIchoice
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def run_math_tests_console_ui():
    math_testsUI.math_tests()

def run_math_tests_gui():
    math_testsGUI.math_tests_gui()

def choose_ToDo_interface():
    print("Welcome to the To-Do List Application!")
    print("Choose the interface you want to use:")
    print("1. Console UI")
    print("2. GUI")
    while True:
        try:
            ToDoUIchoice = int(input("Enter your choice (1 or 2): "))
            if ToDoUIchoice in [1, 2]:
                return ToDoUIchoice
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def run_ToDo_console_ui():
    todolistUI.todo()

def run_ToDo_gui():
    import todolistGUI

def choose_compression_interface():
    print("Welcome to the Compression Tool!")
    print("Choose the interface you want to use:")
    print("1. Console UI")
    print("2. GUI")
    while True:
        try:
            CompressionUIchoice = int(input("Enter your choice (1 or 2): "))
            if CompressionUIchoice in [1, 2]:
                return CompressionUIchoice
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def run_compression_console_ui():
    compression()

def choose_quiz_interface():
    print("Welcome to the Quiz Application!")
    print("Choose the interface you want to use:")
    print("1. Console UI")
    print("2. GUI")
    while True:
        try:
            QuizUIchoice = int(input("Enter your choice (1 or 2): "))
            if QuizUIchoice in [1, 2]:
                return QuizUIchoice
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def choose_work_with_txt_interface():
    print("Welcome to the program!")
    print("Choose the interface you want to use:")
    print("1. Console UI")
    print("2. GUI")
    while True:
        try:
            work_with_txt_UI_choice = int(input("Enter your choice (1 or 2): "))
            if work_with_txt_UI_choice in [1, 2]:
                return work_with_txt_UI_choice
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    print("Welcome to the program!")

    print("Choose the interface you want to use for the Authentication System:")
    print("1. Console UI")
    print("2. GUI")
    while True:
        try:
            auth_choice = int(input("Enter your choice (1 or 2): "))
            if auth_choice in [1, 2]:
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if auth_choice == 1:
        LogManager.log_activity("Console UI for Authentication System opened", "Authentication System")
        run_auth_ui()
    elif auth_choice == 2:
        LogManager.log_activity("GUI for Authentication System opened", "Authentication System")
        run_auth_gui()


    print("Choose the program to run:")
    print("1. Math Tests - You can test your math skills with this program. You will be given a series of math questions you choose to solve and gain score.")
    print("2. Compression of a text file - You can compress a text file by replacing words with abbreviations.")
    print("3. To-Do List - You can manage your tasks with this program.")
    print("4. Quiz - You can create and take quizzes with this program.")
    print("5. Work with txt files - You can read, write, delete, rename, copy, move, or add text to files. You can also count the number of words, lines, characters, special characters, digits, and spaces in a file.")

    while True:
        try:
            choice = int(input("Enter the number of the program you want to run: "))
            if choice in [1, 2, 3, 4, 5]:
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if choice == 1:
        LogManager.log_activity("Math Tests opened", "Math Tests")
        MathTestsUIchoice = choose_math_tests_interface()
        if MathTestsUIchoice == 1:
            LogManager.log_activity("Console UI for Math Tests opened", "Math Tests")
            run_math_tests_console_ui()
        elif MathTestsUIchoice == 2:
            LogManager.log_activity("GUI for Math Tests opened", "Math Tests")
            run_math_tests_gui()
    elif choice == 2:
        LogManager.log_activity("Compression program opened", "Compression")
        CompressionUIchoice = choose_compression_interface()
        if CompressionUIchoice == 1:
            LogManager.log_activity("Console UI for Compression opened", "Compression")
            run_compression_console_ui()
        elif CompressionUIchoice == 2:
            LogManager.log_activity("GUI for Compression opened", "Compression")
            run_compression_gui()
    elif choice == 3:
        LogManager.log_activity("To-Do List started", "To-Do List")
        ToDoUIchoice = choose_ToDo_interface()
        if ToDoUIchoice == 1:
            LogManager.log_activity("Console UI for ToDo list opened", "To-Do List")
            run_ToDo_console_ui()
        elif ToDoUIchoice == 2:
            LogManager.log_activity("GUI for ToDo list opened", "To-Do List")
            run_ToDo_gui()
    elif choice == 4:
        LogManager.log_activity("Quiz Application started", "Quiz")
        QuizUIchoice = choose_quiz_interface()
        if QuizUIchoice == 1:
            LogManager.log_activity("Console UI for Quiz opened", "Quiz")
            run_quizUI()
        elif QuizUIchoice == 2:
            LogManager.log_activity("GUI for Quiz opened", "Quiz")
            run_quiz_GUI()
    elif choice == 5:
        LogManager.log_activity("Work with txt files program started", "Work with txt files")
        work_with_txt_UI_choice = choose_work_with_txt_interface()
        if work_with_txt_UI_choice == 1:
            LogManager.log_activity("Console UI for Work with txt files opened", "Work with txt files")
            work_with_txt()
        elif work_with_txt_UI_choice == 2:
            LogManager.log_activity("GUI for Work with txt files opened", "Work with txt files")
            run_work_with_txtGUI()
    else:
        print("Invalid choice.")

print("Do you want to print the log?")
print("1. Yes")
print("2. No")
while True:
    try:
        print_log = int(input("Enter your choice: "))
        if print_log in [1, 2]:
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if print_log == 1:
    print("Do you want to print log into console or in GUI?")
    print("1. Console")
    print("2. GUI")
    while True:
        try:
            print_log_choice = int(input("Enter your choice: "))
            if print_log_choice in [1, 2]:
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if print_log_choice == 1:
        LogManager.print_log()
    elif print_log_choice == 2:
        run_log_manager_gui()
else:
    print("The log file has not been printed.")
    