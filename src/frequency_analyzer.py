from collections import Counter

class FrequencyAnalyzer:
    """
    A class for analyzing the frequency of words in a given text.
    """

    @staticmethod
    def analyze(text):
        """
        Analyzes the frequency of words in the given text.

        Args:
            text (str): The text to analyze.

        Returns:
            Counter: A Counter object containing the word counts.
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        
        if not text:
            return Counter()
        
        words = text.split()
        word_counts = Counter(words)
        return word_counts
