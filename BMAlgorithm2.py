class BMAlgorithm2:
    def __init__(self):
        pass


    def __str__(self):
        return "BM_Algorithm_2"


    @staticmethod
    def run_algorithm(pattern, text):
        pattern_length = len(pattern)
        text_length = len(text)
        pattern_index = 0
        text_index = 0

        results = []

        if (pattern and text):
            right = BMAlgorithm2._right_array(pattern)

            while (text_index <= text_length - pattern_length):
                skip = 0
                for pattern_index in range(pattern_length - 1, -1, -1):
                    if (text[text_index + pattern_index] != pattern[pattern_index]):
                        skip = max(1, pattern_index - right[text[text_index + pattern_index]])
                        text_index += skip
                        break 
                
                if (skip == 0):
                    results.append(text_index)
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
            right = BMAlgorithm2._right_array(pattern)

            while (text_index <= text_length - pattern_length):
                skip = 0
                for pattern_index in range(pattern_length - 1, -1, -1):
                    if (text[text_index + pattern_index] != pattern[pattern_index]):
                        skip = max(1, pattern_index - right[text[text_index + pattern_index]])
                        text_index += skip
                        break 
                
                if (skip == 0):
                    return text_index

        return None


    def _right_array(pattern):
        pattern_length = len(pattern)

        right = {'\n': -1, ' ': -1, ',': -1, '.': -1, '…': -1, '-': -1, '–': -1, '—': -1, '/': -1,
                ':': -1, ';': -1, '?': -1, '!': -1, '*': -1, '(': -1, ')': -1, '«': -1, '»': -1,
                'A': -1, 'Ą': -1, 'À': -1, 'Æ': -1, 'B': -1, 'C': -1, 'Ć': -1, 'D': -1, 'E': -1,
                'Ę': -1, 'É': -1, 'F': -1, 'G': -1, 'H': -1, 'I': -1, 'J': -1, 'K': -1, 'L': -1,
                'Ł': -1, 'M': -1, 'N': -1, 'Ń': -1, 'O': -1, 'Ó': -1, 'P': -1, 'Q': -1, 'R': -1,
                'S': -1, 'Ś': -1, 'T': -1, 'U': -1, 'V': -1, 'W': -1, 'X': -1, 'Y': -1, 'Z': -1,
                'Ż': -1, 'Ź': -1, '0': -1, '1': -1, '2': -1, '3': -1, '4': -1, '5': -1, '6': -1, 
                '7': -1, '8': -1, '9': -1}

        for pattern_index in range(pattern_length):
            right[pattern[pattern_index]] = pattern_index

        return right