from collections import Counter

# frequency_analyzer.py

class FrequencyAnalyzer:

    @staticmethod
    def analyze(text):
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        
        if not text:
            return Counter()
        
        words = text.split()
        word_counts = Counter(words)
        return word_counts
