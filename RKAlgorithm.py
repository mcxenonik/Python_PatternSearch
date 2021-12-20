class RKAlgorithm:
    def __init__(self):
        pass


    def __str__(self):
        return "RKAlgorithm"


    @staticmethod
    def run_algorithm(pattern, text):
        d = 66
        q = 997

        pattern_length = len(pattern)
        text_length = len(text)
        pattern_index = 0
        text_index = 0
        pattern_hash = 0
        text_hash = 0
        h = 1

        if (pattern and text and text_length >= pattern_length):
            for pattern_index in range(pattern_length - 1):
                h = (h * d) % q

            # Calculate hash value for pattern and text
            for pattern_index in range(pattern_length):
                pattern_hash = (d * pattern_hash + ord(pattern[pattern_index])) % q
                text_hash = (d * text_hash + ord(text[pattern_index])) % q

            # Find the match
            for text_index in range(text_length - pattern_length + 1):
                if (pattern_hash == text_hash):
                    for pattern_index in range(pattern_length):
                        if (text[text_index + pattern_index] != pattern[pattern_index]):
                            break

                    pattern_index += 1
                    if (pattern_index == pattern_length):
                        return text_index

                if (text_index < text_length - pattern_length):
                    text_hash = (d * (text_hash - ord(text[text_index]) * h) + ord(text[text_index + pattern_length])) % q

                    if (text_hash < 0):
                        text_hash += q

        return None