from math_tests import math_tests
from compression import compression
from todolist import todo


if __name__ == "__main__":
    print("Choose the program to run:")
    print("1. Math Tests - You can test your math skills with this program. You will be given a series of math questions you choose to solve and gain score.")
    print("2. Compression of a text file - You can compress a text file by replacing words with abbreviations.")
    print("3. To-Do List - You can manage your tasks with this program.")

    choice = input("Enter the number of the program you want to run: ")
    if choice == "1":
        math_tests()
    elif choice == "2":
        compression()
    elif choice == "3":
        todo()	
    else:
        print("Invalid choice.")