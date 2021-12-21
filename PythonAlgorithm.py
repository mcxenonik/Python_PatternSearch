class PythonAlgorithm:
    def __init__(self):
        pass


    def __str__(self):
        return "Python_Algorithm"


    @staticmethod
    def run_algorithm(pattern, text):
        text_index = 0
        results = []

        if (pattern and text):
            while True:
                text_index = text.find(pattern, text_index)

                if (text_index == -1):
                    break
                else:
                    results.append(text_index)
                    text_index += 1

        if (results):
            return results
        else:
            return None


    @staticmethod
    def run_algorithm2(pattern, text):
        if (pattern and text):
            text_index = text.find(pattern)
            if (text_index != -1):
                return text_index

        return None