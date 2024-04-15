from log_manager import LogManager

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

    @staticmethod
    def get_input_file():
        while True:
            try:
                input_file_path = input("Enter the path to the input file: ")

                # Check the file extension
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
