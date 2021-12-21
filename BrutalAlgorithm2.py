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

        results = []

        if (pattern and text):
            while (text_index < text_length):
                if (text[text_index] == pattern[pattern_index]):
                    pattern_index += 1
                else:
                    text_index -= pattern_index
                    pattern_index = 0

                text_index += 1

                if (pattern_index == pattern_length):
                    results.append(text_index - pattern_length)
                    text_index -= pattern_index
                    pattern_index = 0
                    text_index += 1
        
        if (results):
            return results
        else:
            return None


    @staticmethod
    def run_algorithm2(pattern, text):
        pattern_length = len(pattern)
        text_length = len(text)
        pattern_index = 0
        text_index = 0

        if (pattern and text):
            while (text_index < text_length and pattern_index < pattern_length):
                if (text[text_index] == pattern[pattern_index]):
                    pattern_index += 1
                else:
                    text_index -= pattern_index
                    pattern_index = 0

                text_index += 1

            if (pattern_index == pattern_length):
                return text_index - pattern_length
        
        return None