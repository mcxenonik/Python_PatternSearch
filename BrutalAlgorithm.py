class BrutalAlgorithm:
    def __init__(self):
        pass


    def __str__(self):
        return "Brutal_Algorithm"


    @staticmethod
    def run_algorithm(pattern, text):
        pattern_length = len(pattern)
        text_length = len(text)
        pattern_index = 0
        text_index = 0 

        results = []

        if (pattern and text):
            for text_index in range(text_length - pattern_length + 1):
                for pattern_index in range(pattern_length):
                    if (text[text_index + pattern_index] != pattern[pattern_index]):
                        pattern_index -= 1
                        break
                
                if (pattern_index == pattern_length - 1):
                    results.append(text_index)
        
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
            for text_index in range(text_length - pattern_length + 1):
                for pattern_index in range(pattern_length):
                    if (text[text_index + pattern_index] != pattern[pattern_index]):
                        pattern_index -= 1
                        break
                
                # pattern_index += 1
                # if (pattern_index == pattern_length):
                if (pattern_index == pattern_length - 1):
                    return text_index
        
        return None