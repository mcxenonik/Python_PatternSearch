class BrutalAlgorithm:
    def __init__(self):
        pass


    def __str__(self):
        return "BrutalAlgorithm"


    @staticmethod
    def run_algorithm(pattern, text):
        m = len(pattern)
        n = len(text)
        i = 0
        j = 0

        if (pattern and text):
            for i in range(n - m + 1):
                for j in range(m):
                    if (text[i + j] != pattern[j]):
                        j -= 1
                        break

                if (j == m - 1):
                    return i
        
        return None
