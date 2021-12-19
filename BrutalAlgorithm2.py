class BrutalAlgorithm2:
    def __init__(self):
        pass


    def __str__(self):
        return "BrutalAlgorithm2"


    @staticmethod
    def run_algorithm(pattern, text):
        pattern_length = len(pattern)
        text_length = len(text)
        pattern_index = 0
        text_index = 0

        if (pattern and text):
            while (text_index < text_length and pattern_index < pattern_length):
                if (text[text_index] == pattern[pattern_index]):
                    pattern_index += 1
                else:
                    pattern_index = 0
                    text_index -= pattern_index

                text_index += 1

            if (pattern_index == pattern_length):
                return text_index - pattern_length
        
        return None