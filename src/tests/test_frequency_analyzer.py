import unittest
from frequency_analyzer import analyze

class TestFrequencyAnalyzer(unittest.TestCase):
    def test_analyze(self):
        # Test case 1: Empty string input
        text = ""
        expected_result = {}
        self.assertEqual(analyze(text), expected_result)

        # Test case 2: Single word input
        text = "hello"
        expected_result = {"hello": 1}
        self.assertEqual(analyze(text), expected_result)

        # Test case 3: Multiple words with repeated words input
        text = "hello world hello"
        expected_result = {"hello": 2, "world": 1}
        self.assertEqual(analyze(text), expected_result)

        # Test case 4: Case sensitivity
        text = "Hello hello HELLO"
        expected_result = {"Hello": 1, "hello": 1, "HELLO": 1}
        self.assertEqual(analyze(text), expected_result)

        # Test case 5: Special characters and numbers
        text = "hello! world 123 hello"
        expected_result = {"hello!": 1, "world": 1, "123": 1, "hello": 1}
        self.assertEqual(analyze(text), expected_result)

        # Test case 6: Non-string input
        text = 123
        with self.assertRaises(TypeError):
            analyze(text)

if __name__ == '__main__':
    unittest.main()