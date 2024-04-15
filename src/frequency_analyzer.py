from collections import Counter

class FrequencyAnalyzer:

    @staticmethod
    def analyze(text):
        words = text.split()
        word_counts = Counter(words)
        return word_counts
