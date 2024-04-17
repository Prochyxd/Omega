import os
import sys
from user_interface import UserInterface
from algorithms import WordReplacer
from frequency_analyzer import FrequencyAnalyzer
from log_manager import LogManager

def compression():
    read_guide = input("Do you want to read the guide? (yes/no): ")
    if read_guide.lower() == "yes":
        UserInterface.show_guide()
        input("Press Enter to continue.")
    
    # Ensure that project_root is in sys.path
    project_root = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(project_root)

    # Get input text
    input_file_path = UserInterface.get_input_file()
    with open(input_file_path, "r", encoding="utf-8") as file:
        input_text = file.read()

    # Print words from the input text
    print("Words in the input text:")
    print(input_text.split())

    # Word frequency analysis
    frequency_analyzer = FrequencyAnalyzer()
    word_counts = frequency_analyzer.analyze(input_text)

    print("-------------------------------------------------------------------------------------------")
    print("Word frequencies:")
    print(word_counts)

    # Get replacement words and their abbreviations
    replacements = UserInterface.get_word_replacements()

    # Replace words according to the configuration
    word_replacer = WordReplacer(replacements)
    compressed_text = word_replacer.replace_words(input_text)

    # Log the activity
    action_details = f"Replaced words: {replacements}"
    LogManager.log_activity("Word Replacement", action_details)

    # Save compressed text to the output file
    output_file_path = UserInterface.get_output_file()
    with open(output_file_path, "w") as file:
        file.write(compressed_text)