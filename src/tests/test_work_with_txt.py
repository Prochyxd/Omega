import unittest
from work_with_txt import *

class TestWorkWithTxt(unittest.TestCase):
    def setUp(self):
            """
            Set up the test environment before each test case.

            This method is called automatically before each test case is executed.
            It creates a test file and writes some content to it.

            """
            self.test_file = "test_file.txt"
            with open(self.test_file, "w") as file:
                file.write("This is a test file.\nIt has multiple lines.\n12345\n!@#$%")

    def tearDown(self):
            """
            Clean up method that is called after each test case.
            Removes the test file if it exists.
            """
            if os.path.exists(self.test_file):
                os.remove(self.test_file)

    def test_read_file(self):
        """
        Test case for the read_file function.

        This test verifies that the read_file function correctly reads the contents of a file and returns them as a string.

        It asserts that the returned string matches the expected content of the test file.

        """
        self.assertEqual(read_file(self.test_file), "This is a test file.\nIt has multiple lines.\n12345\n!@#$%")

    def test_write_file(self):
        """
        Test case for the write_file function.

        This test verifies that the write_file function correctly writes new content to a file
        and that the content can be read back from the file.

        It asserts that the return value of write_file is "Text written to file" and that
        the content read from the file is equal to the new content.

        """
        self.assertEqual(write_file(self.test_file, "New content"), "Text written to file")
        self.assertEqual(read_file(self.test_file), "New content")

    def test_delete_file(self):
        """
        Test case for the delete_file function.

        This test verifies the behavior of the delete_file function when deleting a file.

        It asserts that the function returns "File deleted" when the file is successfully deleted,
        and "File not found" when the file does not exist.

        """
        self.assertEqual(delete_file(self.test_file), "File deleted")
        self.assertEqual(delete_file(self.test_file), "File not found")

    def test_rename_file(self):
        """
        Test case for the rename_file function.

        This test verifies that the rename_file function correctly renames a file and updates the file system accordingly.

        It performs the following steps:
        1. Calls the rename_file function with the test_file and a new name.
        2. Asserts that the function returns "File renamed".
        3. Asserts that the new file name exists in the file system.
        4. Calls the rename_file function with the new file name and the original test_file name.
        5. Asserts that the function returns "File renamed".
        6. Asserts that the original test_file name exists in the file system.

        If any of the assertions fail, the test case will fail.

        """
        self.assertEqual(rename_file(self.test_file, "new_test_file.txt"), "File renamed")
        self.assertTrue(os.path.exists("new_test_file.txt"))
        self.assertEqual(rename_file("new_test_file.txt", self.test_file), "File renamed")
        self.assertTrue(os.path.exists(self.test_file))

    def test_copy_file(self):
        """
        Test case for the copy_file function.

        This test verifies that the copy_file function successfully copies a file and
        that the copied file exists.

        It asserts that the return value of the copy_file function is "File copied"
        and checks if the copied file exists using the os.path.exists function.
        """
        self.assertEqual(copy_file(self.test_file, "copy_test_file.txt"), "File copied")
        self.assertTrue(os.path.exists("copy_test_file.txt"))

    def test_move_file(self):
        """
        Test case for the move_file function.

        This test verifies that the move_file function correctly moves a file from one location to another.
        It checks that the file is moved successfully, and that the original file no longer exists.

        """
        self.assertEqual(move_file(self.test_file, "move_test_file.txt"), "File moved")
        self.assertTrue(os.path.exists("move_test_file.txt"))
        self.assertFalse(os.path.exists(self.test_file))

    def test_add_text(self):
        """
        Test case to verify the functionality of the add_text function.

        It asserts that the add_text function adds the provided text to the test file
        and returns the expected result. It also asserts that the read_file function
        returns the expected content of the test file after the text is added.
        """
        self.assertEqual(add_text(self.test_file, "\nAdditional content"), "Text added to file")
        self.assertEqual(read_file(self.test_file), "This is a test file.\nIt has multiple lines.\n12345\n!@#$%\nAdditional content")

    def test_count_words(self):
        """
        Test case for the count_words function.

        This test verifies that the count_words function correctly counts the number of words in a file.

        It asserts that the result of calling count_words with the test_file is equal to the expected output.

        """
        self.assertEqual(count_words(self.test_file), "Number of words in file: 11")

    def test_count_lines(self):
        """
        Test case to verify the count_lines function.

        This test case asserts that the count_lines function returns the expected result
        when given a test file. It checks if the number of lines in the file matches the
        expected value.

        """
        self.assertEqual(count_lines(self.test_file), "Number of lines in file: 4")

    def test_count_characters(self):
        """
        Test case to verify the count_characters function.

        This test case checks if the count_characters function correctly counts the number of characters in a file.
        It asserts that the returned value matches the expected result.

        """
        self.assertEqual(count_characters(self.test_file), "Number of characters in file: 55")

    def test_count_special_characters(self):
        """
        Test case for the count_special_characters function.

        This test verifies that the count_special_characters function correctly counts the number of special characters
        in the given file.

        It asserts that the expected result is equal to the actual result returned by the function.

        """
        self.assertEqual(count_special_characters(self.test_file), "Number of special characters in file: 7")

    def test_count_digits(self):
        """
        Test case to verify the count_digits function.

        This test case checks if the count_digits function correctly counts the number of digits in a file.
        It asserts that the result of count_digits(self.test_file) is equal to "Number of digits in file: 5".
        """
        self.assertEqual(count_digits(self.test_file), "Number of digits in file: 5")

    def test_count_spaces(self):
        """
        Test case to verify the count_spaces function.

        This test case checks if the count_spaces function correctly counts the number of spaces in a file.
        It asserts that the result of count_spaces function is equal to the expected number of spaces in the file.

        """
        self.assertEqual(count_spaces(self.test_file), "Number of spaces in file: 10")

        
    def test_read_empty_file(self):
        """
        Test case to verify the behavior of the read_file function when reading an empty file.
        """
        empty_file = "empty_file.txt"
        with open(empty_file, "w") as file:
            pass

        self.assertEqual(read_file(empty_file), "File is empty")

        os.remove(empty_file)

    def test_read_nonexistent_file(self):
        """
        Test case to verify the behavior of the read_file function when given a nonexistent file.
        """
        nonexistent_file = "nonexistent_file.txt"

        self.assertEqual(read_file(nonexistent_file), "File not found")

    def test_write_file(self):
        """
        Test case for the write_file function.

        This test verifies that the write_file function correctly writes the given content to a file,
        and that the content can be read back from the file.

        Steps:
        1. Create a test file and define its content.
        2. Call the write_file function with the test file and content.
        3. Assert that the function returns "Text written to file".
        4. Assert that the content of the test file matches the original content.
        5. Remove the test file.

        """
        test_file = "test_file.txt"
        content = "This is a test file."

        self.assertEqual(write_file(test_file, content), "Text written to file")
        self.assertEqual(read_file(test_file), content)

        os.remove(test_file)

    def test_delete_nonexistent_file(self):
        """
        Test case to verify the behavior of the delete_file function when trying to delete a nonexistent file.
        """
        nonexistent_file = "nonexistent_file.txt"

        self.assertEqual(delete_file(nonexistent_file), "File not found")

    def test_rename_nonexistent_file(self):
        """
        Test case to verify the behavior of the rename_file function when trying to rename a nonexistent file.

        It asserts that the rename_file function returns the string "File not found" when attempting to rename a file that doesn't exist.
        """
        nonexistent_file = "nonexistent_file.txt"
        new_name = "new_test_file.txt"

        self.assertEqual(rename_file(nonexistent_file, new_name), "File not found")

    def test_copy_nonexistent_file(self):
        """
        Test case to verify the behavior of the copy_file function when trying to copy a nonexistent file.

        It creates a nonexistent_file variable with the name of a file that doesn't exist.
        It also creates a new_path variable with the name of the destination file.
        Then it calls the copy_file function with the nonexistent_file and new_path as arguments.
        Finally, it asserts that the return value of the copy_file function is "File not found".
        """
        nonexistent_file = "nonexistent_file.txt"
        new_path = "copy_test_file.txt"

        self.assertEqual(copy_file(nonexistent_file, new_path), "File not found")

    def test_move_nonexistent_file(self):
        """
        Test case to verify the behavior of the move_file function when trying to move a nonexistent file.

        It creates a nonexistent file and attempts to move it to a new path. The expected behavior is that the
        move_file function should return the string "File not found".

        This test case helps ensure that the move_file function handles nonexistent files correctly.

        """
        nonexistent_file = "nonexistent_file.txt"
        new_path = "move_test_file.txt"

        self.assertEqual(move_file(nonexistent_file, new_path), "File not found")

    def test_add_text_to_empty_file(self):
        """
        Test case to verify that text can be added to an empty file.

        Steps:
        1. Create an empty file.
        2. Add text to the file using the add_text function.
        3. Verify that the text was added successfully.
        4. Verify that the content of the file matches the added text.
        5. Remove the file.

        Expected Result:
        - The add_text function should return "Text added to file".
        - The content of the file should match the added text.
        """

        empty_file = "empty_file.txt"
        text = "Additional content"

        with open(empty_file, "w") as file:
            pass

        self.assertEqual(add_text(empty_file, text), "Text added to file")
        self.assertEqual(read_file(empty_file), text)

        os.remove(empty_file)

if __name__ == "__main__":
    unittest.main()
