import os
import shutil
import re

def read_file(file_path):
    """
    Read the contents of a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The content of the file if it exists and is not empty.
        str: "File is empty" if the file exists but is empty.
        str: "File not found" if the file does not exist.
        str: "Error: <exception>" if any other error occurs while reading the file.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            if content:
                return content
            else:
                return "File is empty"
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return "Error: " + str(e)

def write_file(file_path, text):
    """
    Write the given text to a file.

    Args:
        file_path (str): The path of the file to write to.
        text (str): The text to write to the file.

    Returns:
        str: A message indicating the result of the operation.
            - If the file is successfully written, it returns "Text written to file".
            - If the file is not found, it returns "File not found".
            - If any other error occurs, it returns "Error: <error message>".
    """
    try:
        with open(file_path, 'w') as file:
            file.write(text)
            return "Text written to file"
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return "Error: " + str(e)

def delete_file(file_path):
    """
    Deletes a file at the specified file path.

    Args:
        file_path (str): The path of the file to be deleted.

    Returns:
        str: A message indicating the result of the deletion.
            - If the file is successfully deleted, the message will be "File deleted".
            - If the file is not found, the message will be "File not found".
            - If an error occurs during the deletion process, the message will be "Error: <error_message>".
    """
    try:
        os.remove(file_path)
        return "File deleted"
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return "Error: " + str(e)

def rename_file(file_path, new_name):
    """
    Renames a file.

    Args:
        file_path (str): The path of the file to be renamed.
        new_name (str): The new name for the file.

    Returns:
        str: A message indicating the result of the file renaming operation.
    """
    try:
        os.rename(file_path, new_name)
        return "File renamed"
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return "Error: " + str(e)

def copy_file(file_path, new_path):
    """
    Copy a file from the given file_path to the new_path.

    Args:
        file_path (str): The path of the file to be copied.
        new_path (str): The destination path where the file will be copied.

    Returns:
        str: A message indicating the status of the file copy operation.
            - If the file is successfully copied, it returns "File copied".
            - If the file is not found, it returns "File not found".
            - If any other error occurs during the copy operation, it returns
              "Error: <error_message>".

    """
    try:
        shutil.copy(file_path, new_path)
        return "File copied"
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return "Error: " + str(e)

def move_file(file_path, new_path):
    """
    Move a file from the given file_path to the new_path.

    Args:
        file_path (str): The path of the file to be moved.
        new_path (str): The new path where the file should be moved to.

    Returns:
        str: A message indicating the result of the file move operation.
            - If the file is successfully moved, the message will be "File moved".
            - If the file is not found at the given file_path, the message will be "File not found".
            - If any other error occurs during the file move operation, the message will be "Error: <error_message>".
    """
    try:
        shutil.move(file_path, new_path)
        return "File moved"
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return "Error: " + str(e)

def add_text(file_path, text):
    """
    Appends the given text to the specified file.

    Args:
        file_path (str): The path to the file.
        text (str): The text to be added to the file.

    Returns:
        str: A message indicating the result of the operation.
            - If the text is successfully added to the file, the message will be "Text added to file".
            - If the file is not found, the message will be "File not found".
            - If an error occurs during the operation, the message will be "Error: <error_message>".
    """
    try:
        with open(file_path, 'a') as file:
            file.write(text)
            return "Text added to file"
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return "Error: " + str(e)

def count_words(file_path):
    """
    Counts the number of words in a given file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: A string indicating the number of words in the file, or an error message if the file is not found or an exception occurs.
    """
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            return "Number of words in file: " + str(len(words))
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return "Error: " + str(e)

def count_lines(file_path):
    """
    Counts the number of lines in a given file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: A string indicating the number of lines in the file, or an error message if the file is not found or an exception occurs.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return "Number of lines in file: " + str(len(lines))
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return "Error: " + str(e)

def count_characters(file_path):
    """
    Counts the number of characters in a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: A string indicating the number of characters in the file.

    Raises:
        FileNotFoundError: If the file specified by `file_path` does not exist.
        Exception: If any other error occurs while reading the file.
    """
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            return "Number of characters in file: " + str(len(text))
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return "Error: " + str(e)

def count_special_characters(file_path):
    """
    Counts the number of special characters in a given file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: A message indicating the number of special characters in the file, or an error message if the file is not found or an exception occurs.
    """
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            special_characters = re.findall(r'[^A-Za-z0-9\s]', text)
            return "Number of special characters in file: " + str(len(special_characters))
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return "Error: " + str(e)

def count_digits(file_path):
    """
    Counts the number of digits in a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: A message indicating the number of digits in the file, or an error message if the file is not found or an error occurs.
    """
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            digits = re.findall(r'[0-9]', text)
            return "Number of digits in file: " + str(len(digits))
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return "Error: " + str(e)

def count_spaces(file_path):
    """
    Counts the number of spaces in a given file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: A string indicating the number of spaces in the file, or an error message if the file is not found or an exception occurs.
    """
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            spaces = re.findall(r'\s', text)
            return "Number of spaces in file: " + str(len(spaces))
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return "Error: " + str(e)
