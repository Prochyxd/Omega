import unittest
from algorithms import WordReplacer

class TestWordReplacer(unittest.TestCase):
    def test_replace_words_single_word(self):
        """
        Test case to verify the functionality of replacing a single word using WordReplacer.

        It creates a WordReplacer object with a dictionary mapping 'hello' to 'hi'.
        Then, it calls the replace_words method with the input 'hello world'.
        Finally, it asserts that the result is 'hi world'.
        """
        replacer = WordReplacer({'hello': 'hi'})
        result = replacer.replace_words('hello world')
        self.assertEqual(result, 'hi world')

    def test_replace_words_multiple_words(self):
        """
        Test case to verify the functionality of replacing multiple words using WordReplacer.

        It creates a WordReplacer object with a dictionary of word replacements.
        Then, it calls the replace_words method with the input string 'hello world'.
        Finally, it asserts that the result is equal to the expected output 'hi planet'.
        """
        replacer = WordReplacer({'hello': 'hi', 'world': 'planet'})
        result = replacer.replace_words('hello world')
        self.assertEqual(result, 'hi planet')

    def test_replace_words_case_sensitive(self):
        """
        Test case for the replace_words method of the WordReplacer class.
        It checks if the replace_words method correctly replaces words in a case-sensitive manner.
        """
        replacer = WordReplacer({'Hello': 'Hi'})
        result = replacer.replace_words('Hello world')
        self.assertEqual(result, 'Hi world')

    def test_replace_words_no_replacements(self):
        """
        Test case to verify the behavior of the replace_words method when no replacements are made.
        """
        replacer = WordReplacer({'foo': 'bar'})
        result = replacer.replace_words('hello world')
        self.assertEqual(result, 'hello world')

    def test_replace_words_empty_text(self):
        """
        Test case to verify the behavior of the replace_words method when given an empty text.
        """
        replacer = WordReplacer({'hello': 'hi'})
        result = replacer.replace_words('')
        self.assertEqual(result, '')

    def test_replace_words_invalid_input(self):
        """
        Test case to verify that a ValueError is raised when invalid input is provided to the replace_words method.
        """
        replacer = WordReplacer({'hello': 'hi'})
        with self.assertRaises(ValueError):
            replacer.replace_words(123)

if __name__ == '__main__':
    unittest.main()