# algorithms.py

class WordReplacer:
    def __init__(self, replacement_dict):
        if not isinstance(replacement_dict, dict):
            raise ValueError("replacement_dict must be a dictionary")
        self.replacement_dict = replacement_dict

    def replace_words(self, text):
        if not isinstance(text, str):
            raise ValueError("text must be a string")
        
        for original, replacement in self.replacement_dict.items():
            if not isinstance(original, str) or not isinstance(replacement, str):
                raise ValueError("original and replacement must be strings")
            text = text.replace(original, replacement)
        
        return text
