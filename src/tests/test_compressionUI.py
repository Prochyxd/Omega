
import unittest
from unittest.mock import patch
import io
import sys
import compressionUI

class TestCompressionUI(unittest.TestCase):
    def test_show_guide(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            compressionUI.UserInterface.show_guide()

            # Check if the correct output was printed
            expected_output = "\nGuide:\n1) Enter the path to the input file. The input file must be a non-empty text file with the .txt extension.\n2) All the words in the input file and their frequencies in the text will be displayed.\n3) Enter a word from the text file that you want to replace, press Enter.\n4) Enter an abbreviation/shortcut for the word you entered before.\n5) Repeat the previous two steps for other words.\n6) Press Enter without entering a word to finish.\n7) Enter the name of the output file with the .txt extension (e.g., example.txt). The output file will be created in the project directory.\n8) The output file contains compressed text.\n9) Choose whether to print the log or not.\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_get_input_file_valid(self):
        # Mock the input function to return a valid file path
        with patch('builtins.input', return_value='/path/to/input.txt'):
            input_file_path = compressionUI.UserInterface.get_input_file()
            self.assertEqual(input_file_path, '/path/to/input.txt')

    def test_get_input_file_invalid_extension(self):
        # Mock the input function to return a file path with invalid extension
        with patch('builtins.input', return_value='/path/to/input.doc'):
            with self.assertRaises(ValueError):
                compressionUI.UserInterface.get_input_file()

    def test_get_input_file_empty_file(self):
        # Mock the input function to return a file path of an empty file
        with patch('builtins.input', return_value='/path/to/empty.txt'):
            with self.assertRaises(ValueError):
                compressionUI.UserInterface.get_input_file()

    def test_get_input_file_nonexistent_file(self):
        # Mock the input function to return a file path of a nonexistent file
        with patch('builtins.input', return_value='/path/to/nonexistent.txt'):
            with self.assertRaises(FileNotFoundError):
                compressionUI.UserInterface.get_input_file()

    def test_get_word_replacements(self):
        # Mock the input function to simulate user input
        with patch('builtins.input', side_effect=['word1', 'abbr1', 'word2', 'abbr2', '']):
            replacements = compressionUI.UserInterface.get_word_replacements()
            expected_replacements = {'word1': 'abbr1', 'word2': 'abbr2'}
            self.assertEqual(replacements, expected_replacements)

    def test_get_output_file_valid(self):
        # Mock the input function to return a valid output file name
        with patch('builtins.input', return_value='output.txt'):
            output_file_path = compressionUI.UserInterface.get_output_file()
            self.assertEqual(output_file_path, 'output.txt')

    def test_get_output_file_invalid_extension(self):
        # Mock the input function to return an output file name with invalid extension
        with patch('builtins.input', return_value='output.doc'):
            with self.assertRaises(ValueError):
                compressionUI.UserInterface.get_output_file()

    def test_compression(self):
        # Mock the input function to simulate user input
        with patch('builtins.input', side_effect=['yes', '', 'word1', 'abbr1', 'word2', 'abbr2', 'output.txt']):
            with patch('builtins.open', create=True) as mock_open:
                # Mock the read method of the file object
                mock_open.return_value.__enter__.return_value.read.return_value = 'input text'

                # Mock the write method of the file object
                mock_file = mock_open.return_value.__enter__.return_value
                mock_file.write.return_value = None

                compressionUI.compression()

                # Check if the expected methods were called
                mock_open.assert_called_once_with('/path/to/input.txt', 'r', encoding='utf-8')
                mock_file.read.assert_called_once()
                mock_file.write.assert_called_once_with('compressed text')
                mock_open.assert_called_with('output.txt', 'w')

if __name__ == '__main__':
    unittest.main()