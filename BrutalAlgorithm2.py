class BrutalAlgorithm2:
    def __init__(self):
        pass


    def __str__(self):
        return "BrutalAlgorithm2"


    @staticmethod
    def run_algorithm(pattern, text):
        m = len(pattern)
        n = len(text)
        i = 0
        j = 0

        if (pattern and text):
            while (i < n and j < m):
                if (text[i] == pattern[j]):
                    j += 1
                else:
                    j = 0
                    i -= j

                i += 1

            if (j == m):
                return i - m
        
        return None