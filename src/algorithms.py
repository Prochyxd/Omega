class WordReplacer:

    def __init__(self, replacement_dict):

        self.replacement_dict = replacement_dict

    def replace_words(self, text):

        for original, replacement in self.replacement_dict.items():
            text = text.replace(original, replacement)
        return text
