#this will be guide printed in console
#the user will be able to look at this guide and understand how to use the program

def run_guide_ui():
    print("Guide in console:")
    print("Do you want to see the overall guide of the program or the guide of a specific part of the program?")
    print("1. Overall guide")
    print("2. Specific guide")
    print("3. Exit")
    while True:
        try:
            guide_choice = int(input("Enter your choice (1, 2 or 3): "))
            if guide_choice in [1, 2, 3]:
                return guide_choice
            else:
                print("Invalid choice. Please enter 1, 2 or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    #this will be the overall guide printed in console
    #the user will be able to look at this guide and understand how to use the program
        if guide_choice == 1:
            print("This program is a collection of different applications.")
            print("There is five applications in this program:")
            print("Math tests, To-Do List, Compression, Quiz and Work with txt.")
            print("You can choose the interface you want to use for each application (Console UI or GUI).")
            print("Enjoy using the program!")
        #this will be the specific guide printed in console
        #the user will be able to look at this guide and understand how to use the program
        elif guide_choice == 2:
            print("Which part of the program do you want to see the guide of?")
            print("1. Math tests")
            print("2. To-Do List")
            print("3. Compression")
            print("4. Quiz")
            print("5. Work with txt")
            while True:
                try:
                    specific_guide_choice = int(input("Enter your choice (1, 2, 3, 4 or 5): "))
                    if specific_guide_choice in [1, 2, 3, 4, 5]:
                        break
                    else:
                        print("Invalid choice. Please enter 1, 2, 3, 4 or 5.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            if specific_guide_choice == 1:
                print("Math tests guide:")
                print("This application is a collection of math tests.")
                print("You can choose the branch and difficulty of the tests.")
                print("You can also choose the interface you want to use (Console UI or GUI).")
                print("Step by step: choose the branch, choose the difficulty, answer the questions and see your score.")
            elif specific_guide_choice == 2:
                print("To-Do List guide:")
                print("This application is a simple To-Do List.")
                print("You can add tasks, mark them as done and delete them.")
                print("You can also choose the interface you want to use (Console UI or GUI).")
                print("Step by step: add a task, mark it as done, delete it.")
            elif specific_guide_choice == 3:
                print("Compression guide:")
                print("This application is a compression program.")
                print("You can also choose the interface you want to use (Console UI or GUI).")
                print("Step by step: choose the file you want to compress, choose the words in the file you want to change, then write the short form of it and compress the file.")
            elif specific_guide_choice == 4:
                print("Quiz guide:")
                print("This application is a quiz application.")
                print("You can make quizzes, take part in them or delete them.")
                print("You can also choose the interface you want to use (Console UI or GUI).")
                print("Step by step: make a quiz, take part in it, see the leaderboard.")
            elif specific_guide_choice == 5:
                print("Work with txt guide:")
                print("This application is a program that allows you to work with txt files.")
                print("You can read, write, copy, delete, rename and many other functions with the text files.")
                print("You can also choose the interface you want to use (Console UI or GUI).")
                print("Step by step: choose the file you want to work with, choose the function you want to use, then do the function.")
        elif guide_choice == 3:
            return 3
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")

