import unittest
from frequency_analyzer import FrequencyAnalyzer

class TestFrequencyAnalyzer(unittest.TestCase):
    def test_analyze_empty_text(self):
        """
        Test case to verify the behavior of the FrequencyAnalyzer.analyze method when given an empty text.
        """
        text = ""
        result = FrequencyAnalyzer.analyze(text)
        self.assertEqual(result, {})

    def test_analyze_single_word(self):
        """
        Test case to verify the behavior of the analyze method when given a single word.
        """
        text = "hello"
        result = FrequencyAnalyzer.analyze(text)
        expected_output = {"hello": 1}
        self.assertEqual(result, expected_output)

    def test_analyze_multiple_words(self):
        """
        Test the analyze method of the FrequencyAnalyzer class when given a string with multiple words.
        """
        text = "hello world hello"
        result = FrequencyAnalyzer.analyze(text)
        expected_output = {"hello": 2, "world": 1}
        self.assertEqual(result, expected_output)

    def test_analyze_non_string_input(self):
        """
        Test case to verify that a TypeError is raised when non-string input is passed to the FrequencyAnalyzer.analyze method.
        """
        text = 123
        with self.assertRaises(TypeError):
            FrequencyAnalyzer.analyze(text)

if __name__ == '__main__':
    unittest.main()