class BMAlgorithm2:
    def __init__(self):
        pass


    def __str__(self):
        return "BMAlgorithm2"


    @staticmethod
    def run_algorithm(pattern, text):
        pattern_length = len(pattern)
        text_length = len(text)
        pattern_index = 0
        text_index = 0

        if (pattern and text):
            right = BMAlgorithm2._right_array(pattern)

            while (text_index <= text_length - pattern_length):
                skip = 0
                for pattern_index in range(pattern_length - 1, -1, -1):
                    if (text[text_index + pattern_index] != pattern[pattern_index]):
                        # skip = max(1, pattern_index - right.get(text[text_index + pattern_index], -1))
                        if (text[text_index + pattern_index] in right):
                            skip = max(1, pattern_index - right[text[text_index + pattern_index]])
                        else:
                            skip = max(1, pattern_index + 1)
                        
                        text_index += skip
                        break 
                
                if (skip == 0):
                    return text_index

        return None

    def _right_array(pattern):
        pattern_length = len(pattern)
        right = {}

        for pattern_index in range(pattern_length):
            right[pattern[pattern_index]] = pattern_index

        return right