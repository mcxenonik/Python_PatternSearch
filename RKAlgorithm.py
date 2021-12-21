class RKAlgorithm:
    def __init__(self):
        pass


    def __str__(self):
        return "RKAlgorithm"


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
            # The value of h would be "pow(d, M-1)% q"
            for pattern_index in range(pattern_length - 1):
                h = (h * d) % q

            # Calculate the hash value of pattern and first window of text
            for pattern_index in range(pattern_length):
                pattern_hash = (d * pattern_hash + ord(pattern[pattern_index])) % q
                text_hash = (d * text_hash + ord(text[pattern_index])) % q

            # Slide the pattern over text one by one
            for text_index in range(text_length - pattern_length + 1):
                # Check the hash values of current window of text and
                # pattern if the hash values match then only check
                # for characters on by one
                if (pattern_hash == text_hash):
                    # Check for characters one by one
                    for pattern_index in range(pattern_length):
                        if (text[text_index + pattern_index] != pattern[pattern_index]):
                            break

                    pattern_index += 1
                    # if p == t and pat[0...M-1] = txt[i, i + 1, ...i + M-1]
                    if (pattern_index == pattern_length):
                        # return text_index
                        results.append(text_index)

                # Calculate hash value for next window of text: Remove
                # leading digit, add trailing digit
                if (text_index < text_length - pattern_length):
                    text_hash = (d * (text_hash - ord(text[text_index]) * h) + ord(text[text_index + pattern_length])) % q

                    # We might get negative values of t, converting it to positive
                    if (text_hash < 0):
                        text_hash += q

        if (len(results) != 0):
            return results
        else:
            return None