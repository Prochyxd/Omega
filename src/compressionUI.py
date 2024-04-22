from log_manager import LogManager
import os
import sys
from algorithms import WordReplacer
from frequency_analyzer import FrequencyAnalyzer

class UserInterface:
    @staticmethod
    def show_guide():
        print("\nGuide:")
        print("1) Enter the path to the input file. The input file must be a non-empty text file with the .txt extension.")
        print("2) All the words in the input file and their frequencies in the text will be displayed.")
        print("3) Enter a word from the text file that you want to replace, press Enter.")
        print("4) Enter an abbreviation/shortcut for the word you entered before.")
        print("5) Repeat the previous two steps for other words.")
        print("6) Press Enter without entering a word to finish.")
        print("7) Enter the name of the output file with the .txt extension (e.g., example.txt). The output file will be created in the project directory.")
        print("8) The output file contains compressed text.")
        print("9) Choose whether to print the log or not.")

    class CompressionUI:
        @staticmethod
        def get_input_file():
            """
            Prompts the user to enter the path to an input file and validates the file.

            Returns:
                str: The path to the input file.

            Raises:
                FileNotFoundError: If the specified file does not exist.
                ValueError: If the specified file is not a .txt file or if it is empty.
            """
            while True:
                try:
                    input_file_path = input("Enter the path to the input file: ")

                    if not input_file_path.endswith('.txt'):
                        raise ValueError("Error: The specified file is not a .txt file.")

                    with open(input_file_path, "r", encoding="utf-8") as file:
                        file_content = file.read()
                        if not file_content:
                            raise ValueError("Error: The specified file is empty.")
                        return input_file_path
                except FileNotFoundError:
                    error_message = "Error: The specified file does not exist. Enter a valid file path."
                    log_file_path = LogManager.log_activity("Error", error_message)
                    print(error_message)
                    print(f"Error has been logged: {log_file_path}")
                except ValueError as e:
                    error_message = str(e)
                    log_file_path = LogManager.log_activity("Error", error_message)
                    print(error_message)
                    print(f"Error has been logged: {log_file_path}")

        @staticmethod
        def get_word_replacements():
            """
            Prompts the user to enter words and their corresponding abbreviations,
            and returns a dictionary of word replacements.

            Returns:
                dict: A dictionary where the keys are words and the values are abbreviations.
            """
            replacements = {}
            while True:
                word = input("Enter the word you want to replace, or press Enter to finish: ")
                if not word:
                    break
                abbreviation = input(f"Enter an abbreviation for the word '{word}': ")
                replacements[word] = abbreviation
            return replacements

        @staticmethod
        def get_output_file():
            """
            Prompts the user to enter the name of the output file with the .txt extension.
            If the specified output file is not a .txt file, an error message is displayed and logged.
            
            Returns:
            - output_file_path (str): The name of the output file with the .txt extension.
            """
            while True:
                output_file_path = input("Enter the name of the output file with the .txt extension: ")
                if output_file_path:
                    if not output_file_path.endswith('.txt'):
                        error_message = "Error: The specified output file is not a .txt file."
                        log_file_path = LogManager.log_activity("Error", error_message)
                        print(error_message)
                        print(f"Error has been logged: {log_file_path}")
                    else:
                        return output_file_path
                else:
                    print("You entered an empty file name. Enter again.")


def compression():
    """
    Perform text compression by replacing words according to user-defined configurations.

    This function prompts the user to read a guide, reads an input text file, performs word frequency analysis,
    replaces words according to user-defined configurations, logs the activity, and saves the compressed text
    to an output file.

    Args:
        None

    Returns:
        None
    """
    read_guide = input("Do you want to read the guide? (yes/no): ")
    if read_guide.lower() == "yes":
        UserInterface.show_guide()
        input("Press Enter to continue.")
    
    project_root = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(project_root)

    input_file_path = UserInterface.get_input_file()
    with open(input_file_path, "r", encoding="utf-8") as file:
        input_text = file.read()

    print("Words in the input text:")
    print(input_text.split())

    frequency_analyzer = FrequencyAnalyzer()
    word_counts = frequency_analyzer.analyze(input_text)

    print("-------------------------------------------------------------------------------------------")
    print("Word frequencies:")
    print(word_counts)

    replacements = UserInterface.get_word_replacements()

    word_replacer = WordReplacer(replacements)
    compressed_text = word_replacer.replace_words(input_text)

    action_details = f"Replaced words: {replacements}"
    LogManager.log_activity("Word Replacement", action_details)

    output_file_path = UserInterface.get_output_file()
    with open(output_file_path, "w") as file:
        file.write(compressed_text)
