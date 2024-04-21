# work_with_txt.py
# This program will let user work with txt files
# It will let user read, write, delete, rename, copy, move, or add text to files
# It will also let user count the number of words in a file
# It will also let user count the number of lines in a file
# It will also let user count the number of characters in a file
# It will also let user count the number of special characters in a file
# It will also let user count the number of digits in a file
# It will also let user count the number of spaces in a file

import os
import shutil
import re

def read_file(file_path):
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
    try:
        with open(file_path, 'w') as file:
            file.write(text)
            return "Text written to file"
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return "Error: " + str(e)

def delete_file(file_path):
    try:
        os.remove(file_path)
        return "File deleted"
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return "Error: " + str(e)

def rename_file(file_path, new_name):
    try:
        os.rename(file_path, new_name)
        return "File renamed"
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return "Error: " + str(e)

def copy_file(file_path, new_path):
    try:
        shutil.copy(file_path, new_path)
        return "File copied"
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return "Error: " + str(e)

def move_file(file_path, new_path):
    try:
        shutil.move(file_path, new_path)
        return "File moved"
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return "Error: " + str(e)

def add_text(file_path, text):
    try:
        with open(file_path, 'a') as file:
            file.write(text)
            return "Text added to file"
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return "Error: " + str(e)

def count_words(file_path):
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
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return "Number of lines in file: " + str(len(lines))
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return "Error: " + str(e)

def count_characters(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            return "Number of characters in file: " + str(len(text))
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return "Error: " + str(e)

def count_special_characters(file_path):
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
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            spaces = re.findall(r'\s', text)
            return "Number of spaces in file: " + str(len(spaces))
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return "Error: " + str(e)
