class RKAlgorithm:
    def __init__(self):
        pass


    def __str__(self):
        return "RK_Algorithm"


    @staticmethod
    def run_algorithm(pattern, text):
        d = 66      # Number of characters in the input alphabet
        q = 101     # A prime number

        pattern_length = len(pattern)
        text_length = len(text)
        pattern_index = 0
        text_index = 0
        pattern_hash = 0
        text_hash = 0
        h = 1

        results = []

        if (pattern and text and text_length >= pattern_length):
            for pattern_index in range(pattern_length - 1):                                         # The value of h would be "pow(d, M-1)% q"
                h = (h * d) % q

            for pattern_index in range(pattern_length):                                             # Calculate the hash value of pattern and first window of text
                pattern_hash = (d * pattern_hash + ord(pattern[pattern_index])) % q
                text_hash = (d * text_hash + ord(text[pattern_index])) % q

            for text_index in range(text_length - pattern_length + 1):                              # Slide the pattern over text one by one
                if (pattern_hash == text_hash):                                                     # Check the hash values of current window of text and pattern if 
                    for pattern_index in range(pattern_length):                                     # the hash values match then only check for characters on by one
                        if (text[text_index + pattern_index] != pattern[pattern_index]):
                            break

                    pattern_index += 1
                    if (pattern_index == pattern_length):                                           # if pattern_hash == text_hash and pattern[0...M-1] = text[i, i + 1, ...i + M-1]
                        results.append(text_index)

                if (text_index < text_length - pattern_length):                                     # Calculate hash value for next window of text: Remove leading digit, add trailing digit
                    text_hash = (d * (text_hash - ord(text[text_index]) * h) + ord(text[text_index + pattern_length])) % q

                    if (text_hash < 0):                                                             # We might get negative values of text_hash, converting it to positive
                        text_hash += q

        if (results):
            return results
        else:
            return None


    @staticmethod
    def run_algorithm2(pattern, text):
        d = 66      # Number of characters in the input alphabet
        q = 101     # A prime number

        pattern_length = len(pattern)
        text_length = len(text)
        pattern_index = 0
        text_index = 0
        pattern_hash = 0
        text_hash = 0
        h = 1

        if (pattern and text and text_length >= pattern_length):
            for pattern_index in range(pattern_length - 1):                                         # The value of h would be "pow(d, M-1)% q"
                h = (h * d) % q

            for pattern_index in range(pattern_length):                                             # Calculate the hash value of pattern and first window of text
                pattern_hash = (d * pattern_hash + ord(pattern[pattern_index])) % q
                text_hash = (d * text_hash + ord(text[pattern_index])) % q

            for text_index in range(text_length - pattern_length + 1):                              # Slide the pattern over text one by one
                if (pattern_hash == text_hash):                                                     # Check the hash values of current window of text and pattern if 
                    for pattern_index in range(pattern_length):                                     # the hash values match then only check for characters on by one
                        if (text[text_index + pattern_index] != pattern[pattern_index]):
                            break

                    pattern_index += 1
                    if (pattern_index == pattern_length):                                           # if pattern_hash == text_hash and pattern[0...M-1] = text[i, i + 1, ...i + M-1]
                        return text_index

                if (text_index < text_length - pattern_length):                                     # Calculate hash value for next window of text: Remove leading digit, add trailing digit
                    text_hash = (d * (text_hash - ord(text[text_index]) * h) + ord(text[text_index + pattern_length])) % q

                    if (text_hash < 0):                                                             # We might get negative values of text_hash, converting it to positive
                        text_hash += q

        return None