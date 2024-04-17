from compression import compression
from log_manager import LogManager
import math_testsUI
import math_testsGUI
import todolistUI


def choose_math_tests_interface():
    print("Welcome to Math Tests!")
    print("Choose the interface you want to use:")
    print("1. Console UI")
    print("2. GUI")
    MathTestsUIchoice = input("Enter your choice (1 or 2): ")
    return MathTestsUIchoice

def run_math_tests_console_ui():
    math_testsUI.math_tests()

def run_math_tests_gui():
    math_testsGUI.math_tests_gui()

def choose_ToDo_interface():
    print("Welcome to the To-Do List Application!")
    print("Choose the interface you want to use:")
    print("1. Console UI")
    print("2. GUI")
    ToDoUIchoice = input("Enter your choice (1 or 2): ")
    return ToDoUIchoice

def run_ToDo_console_ui():
    todolistUI.todo()

def run_ToDo_gui():
    import todolistGUI

if __name__ == "__main__":
    print("Choose the program to run:")
    print("1. Math Tests - You can test your math skills with this program. You will be given a series of math questions you choose to solve and gain score.")
    print("2. Compression of a text file - You can compress a text file by replacing words with abbreviations.")
    print("3. To-Do List - You can manage your tasks with this program.")

    choice = input("Enter the number of the program you want to run: ")
    if choice == "1":
        LogManager.log_activity("Math Tests opened", "Math Tests")
        MathTestsUIchoice = choose_math_tests_interface()
        if MathTestsUIchoice == "1":
            LogManager.log_activity("Console UI for Math Tests opened", "Math Tests")
            run_math_tests_console_ui()
        elif MathTestsUIchoice == "2":
            LogManager.log_activity("GUI for Math Tests opened", "Math Tests")
            run_math_tests_gui()
        else:
            print("Invalid choice. Please enter 1 or 2.")
    elif choice == "2":
        compression()
        LogManager.log_activity("Compression program opened", "Compression")
    elif choice == "3":
        LogManager.log_activity("To-Do List started", "To-Do List")
        ToDoUIchoice = choose_ToDo_interface()
        if ToDoUIchoice == "1":
            LogManager.log_activity("Console UI for ToDo list opened", "To-Do List")
            run_ToDo_console_ui()
        elif ToDoUIchoice == "2":
            LogManager.log_activity("GUI for ToDo list opened", "To-Do List")
            run_ToDo_gui()
        else:
            print("Invalid choice. Please enter 1 or 2.")
    else:
        print("Invalid choice.")

    # Print the log
    print("-------------------------------------------------------------------------------------------")
    print("Do you want to print the log? (yes/no): ")
    print_log = input()
    if print_log.lower() == "yes":
        LogManager.print_log()
