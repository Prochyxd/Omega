import unittest
from frequency_analyzer import FrequencyAnalyzer

class TestFrequencyAnalyzer(unittest.TestCase):
    def test_analyze_empty_text(self):
        text = ""
        result = FrequencyAnalyzer.analyze(text)
        self.assertEqual(result, {})

    def test_analyze_single_word(self):
        text = "hello"
        result = FrequencyAnalyzer.analyze(text)
        expected_output = {"hello": 1}
        self.assertEqual(result, expected_output)

    def test_analyze_multiple_words(self):
        text = "hello world hello"
        result = FrequencyAnalyzer.analyze(text)
        expected_output = {"hello": 2, "world": 1}
        self.assertEqual(result, expected_output)

    def test_analyze_non_string_input(self):
        text = 123
        with self.assertRaises(TypeError):
            FrequencyAnalyzer.analyze(text)

if __name__ == '__main__':
    unittest.main()