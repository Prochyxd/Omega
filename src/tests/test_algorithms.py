import unittest
from algorithms import WordReplacer

class TestWordReplacer(unittest.TestCase):
    def setUp(self):
        self.replacement_dict = {"hello": "hi", "world": "earth"}
        self.word_replacer = WordReplacer(self.replacement_dict)

    def test_replace_words(self):
        text = "hello world"
        expected_output = "hi earth"
        self.assertEqual(self.word_replacer.replace_words(text), expected_output)

    def test_replace_words_with_empty_text(self):
        text = ""
        expected_output = ""
        self.assertEqual(self.word_replacer.replace_words(text), expected_output)

    def test_replace_words_with_no_replacements(self):
        text = "hello world"
        word_replacer = WordReplacer({})
        self.assertEqual(word_replacer.replace_words(text), text)

    def test_replace_words_with_non_string_text(self):
        text = 123
        with self.assertRaises(ValueError):
            self.word_replacer.replace_words(text)

    def test_replace_words_with_non_string_replacements(self):
        replacement_dict = {"hello": 123, "world": "earth"}
        with self.assertRaises(ValueError):
            WordReplacer(replacement_dict)

    def test_replace_words_with_non_dict_replacements(self):
        replacement_dict = ["hello", "world"]
        with self.assertRaises(ValueError):
            WordReplacer(replacement_dict)

if __name__ == '__main__':
    unittest.main()