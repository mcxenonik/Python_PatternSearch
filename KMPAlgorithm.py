class KMPAlgorithm:
    def __init__(self):
        pass


    def __str__(self):
        return "KMPAlgorithm"


    @staticmethod
    def run_algorithm(pattern, text):
        pattern_length = len(pattern)
        text_length = len(text)
        pattern_index = 0
        text_index = 0

        results = []
        
        if (pattern and text):
            dfa = KMPAlgorithm._dfa_array(pattern)

            while (text_index < text_length):
                # pattern_index = dfa.get(text[text_index], [0])[pattern_index]
                if (text[text_index] in dfa):
                    pattern_index = dfa[text[text_index]][pattern_index]
                else:
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
            dfa = KMPAlgorithm._dfa_array(pattern)

            while (text_index < text_length and pattern_index < pattern_length):
                # pattern_index = dfa.get(text[text_index], [0])[pattern_index]
                if (text[text_index] in dfa):
                    pattern_index = dfa[text[text_index]][pattern_index]
                else:
                    pattern_index = 0

                text_index += 1
               
            if (pattern_index == pattern_length):
                return text_index - pattern_length
        
        return None


    def _dfa_array(pattern):
        pattern_length = len(pattern)
        dfa = {}
        x = 0

        for char in pattern:
            if (char not in dfa):
                dfa[char] = [0 for i in range(pattern_length)]
 
        dfa[pattern[0]][0] = 1    

        for pattern_index in range(1, pattern_length):
            for c in dfa:                                                       # DLA KAŻDEJ LITERY ALFABETU
                dfa[c][pattern_index] = dfa[c][x]                               # PRZEJŚCIA NIE PASUJĄCE

            dfa[pattern[pattern_index]][pattern_index] = pattern_index + 1      # PRZEJŚCIA PASUJĄCE
            x = dfa[pattern[pattern_index]][x]                                  # AKTUALIZACJA STANU "PONOWNEGO URUCHAMIANIA"

        return dfa