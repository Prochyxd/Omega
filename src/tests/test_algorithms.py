import unittest
from algorithms import WordReplacer

class TestWordReplacer(unittest.TestCase):
    def test_replace_words_single_word(self):
        replacer = WordReplacer({'hello': 'hi'})
        result = replacer.replace_words('hello world')
        self.assertEqual(result, 'hi world')

    def test_replace_words_multiple_words(self):
        replacer = WordReplacer({'hello': 'hi', 'world': 'planet'})
        result = replacer.replace_words('hello world')
        self.assertEqual(result, 'hi planet')

    def test_replace_words_case_sensitive(self):
        replacer = WordReplacer({'Hello': 'Hi'})
        result = replacer.replace_words('Hello world')
        self.assertEqual(result, 'Hi world')

    def test_replace_words_no_replacements(self):
        replacer = WordReplacer({'foo': 'bar'})
        result = replacer.replace_words('hello world')
        self.assertEqual(result, 'hello world')

    def test_replace_words_empty_text(self):
        replacer = WordReplacer({'hello': 'hi'})
        result = replacer.replace_words('')
        self.assertEqual(result, '')

    def test_replace_words_invalid_input(self):
        replacer = WordReplacer({'hello': 'hi'})
        with self.assertRaises(ValueError):
            replacer.replace_words(123)

if __name__ == '__main__':
    unittest.main()