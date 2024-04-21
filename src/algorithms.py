# algorithms.py

class WordReplacer:
    """
    A class that replaces words in a given text based on a replacement dictionary.

    Args:
        replacement_dict (dict): A dictionary containing the original words as keys and their replacements as values.

    Raises:
        ValueError: If `replacement_dict` is not a dictionary.

    Attributes:
        replacement_dict (dict): The dictionary containing the original words and their replacements.

    Methods:
        replace_words(text): Replaces the words in the given text based on the replacement dictionary.

    """

    def __init__(self, replacement_dict):
        if not isinstance(replacement_dict, dict):
            raise ValueError("replacement_dict must be a dictionary")
        self.replacement_dict = replacement_dict

    def replace_words(self, text):
        """
        Replaces the words in the given text based on the replacement dictionary.

        Args:
            text (str): The text in which the words will be replaced.

        Raises:
            ValueError: If `text` is not a string.

        Returns:
            str: The text with the words replaced.

        """
        if not isinstance(text, str):
            raise ValueError("text must be a string")
        
        for original, replacement in self.replacement_dict.items():
            if not isinstance(original, str) or not isinstance(replacement, str):
                raise ValueError("original and replacement must be strings")
            text = text.replace(original, replacement)
        
        return text
