# test_work_with_txt.py
import unittest
from work_with_txt import *

class TestWorkWithTxt(unittest.TestCase):
    def setUp(self):
        # Create a test file and write some content for testing
        self.test_file = "test_file.txt"
        with open(self.test_file, "w") as file:
            file.write("This is a test file.\nIt has multiple lines.\n12345\n!@#$%")

    def tearDown(self):
        # Remove the test file after each test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_read_file(self):
        self.assertEqual(read_file(self.test_file), "This is a test file.\nIt has multiple lines.\n12345\n!@#$%")

    def test_write_file(self):
        self.assertEqual(write_file(self.test_file, "New content"), "Text written to file")
        self.assertEqual(read_file(self.test_file), "New content")

    def test_delete_file(self):
        self.assertEqual(delete_file(self.test_file), "File deleted")
        self.assertEqual(delete_file(self.test_file), "File not found")

    def test_rename_file(self):
        self.assertEqual(rename_file(self.test_file, "new_test_file.txt"), "File renamed")
        self.assertTrue(os.path.exists("new_test_file.txt"))
        self.assertEqual(rename_file("new_test_file.txt", self.test_file), "File renamed")
        self.assertTrue(os.path.exists(self.test_file))

    def test_copy_file(self):
        self.assertEqual(copy_file(self.test_file, "copy_test_file.txt"), "File copied")
        self.assertTrue(os.path.exists("copy_test_file.txt"))

    def test_move_file(self):
        self.assertEqual(move_file(self.test_file, "move_test_file.txt"), "File moved")
        self.assertTrue(os.path.exists("move_test_file.txt"))
        self.assertFalse(os.path.exists(self.test_file))

    def test_add_text(self):
        self.assertEqual(add_text(self.test_file, "\nAdditional content"), "Text added to file")
        self.assertEqual(read_file(self.test_file), "This is a test file.\nIt has multiple lines.\n12345\n!@#$%\nAdditional content")

    def test_count_words(self):
        self.assertEqual(count_words(self.test_file), "Number of words in file: 11")

    def test_count_lines(self):
        self.assertEqual(count_lines(self.test_file), "Number of lines in file: 4")

    def test_count_characters(self):
        self.assertEqual(count_characters(self.test_file), "Number of characters in file: 55")

    def test_count_special_characters(self):
        self.assertEqual(count_special_characters(self.test_file), "Number of special characters in file: 7")

    def test_count_digits(self):
        self.assertEqual(count_digits(self.test_file), "Number of digits in file: 5")

    def test_count_spaces(self):
        self.assertEqual(count_spaces(self.test_file), "Number of spaces in file: 10")

        
    def test_read_empty_file(self):
        # Test reading an empty file
        empty_file = "empty_file.txt"
        with open(empty_file, "w") as file:
            pass  # Create an empty file

        self.assertEqual(read_file(empty_file), "File is empty")

        os.remove(empty_file)

    def test_read_nonexistent_file(self):
        # Test reading a nonexistent file
        nonexistent_file = "nonexistent_file.txt"

        self.assertEqual(read_file(nonexistent_file), "File not found")

    def test_write_file(self):
        # Test writing to a file
        test_file = "test_file.txt"
        content = "This is a test file."

        self.assertEqual(write_file(test_file, content), "Text written to file")
        self.assertEqual(read_file(test_file), content)

        os.remove(test_file)

    def test_delete_nonexistent_file(self):
        # Test deleting a nonexistent file
        nonexistent_file = "nonexistent_file.txt"

        self.assertEqual(delete_file(nonexistent_file), "File not found")

    def test_rename_nonexistent_file(self):
        # Test renaming a nonexistent file
        nonexistent_file = "nonexistent_file.txt"
        new_name = "new_test_file.txt"

        self.assertEqual(rename_file(nonexistent_file, new_name), "File not found")

    def test_copy_nonexistent_file(self):
        # Test copying a nonexistent file
        nonexistent_file = "nonexistent_file.txt"
        new_path = "copy_test_file.txt"

        self.assertEqual(copy_file(nonexistent_file, new_path), "File not found")

    def test_move_nonexistent_file(self):
        # Test moving a nonexistent file
        nonexistent_file = "nonexistent_file.txt"
        new_path = "move_test_file.txt"

        self.assertEqual(move_file(nonexistent_file, new_path), "File not found")

    def test_add_text_to_empty_file(self):
        # Test adding text to an empty file
        empty_file = "empty_file.txt"
        text = "Additional content"

        with open(empty_file, "w") as file:
            pass  # Create an empty file

        self.assertEqual(add_text(empty_file, text), "Text added to file")
        self.assertEqual(read_file(empty_file), text)

        os.remove(empty_file)

if __name__ == "__main__":
    unittest.main()
