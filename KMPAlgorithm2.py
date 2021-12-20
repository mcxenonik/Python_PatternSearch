class KMPAlgorithm2:
    def __init__(self):
        pass


    def __str__(self):
        return "KMPAlgorithm2"


    @staticmethod
    def run_algorithm(pattern, text):
        pattern_length = len(pattern)
        text_length = len(text)
        pattern_index = 0
        text_index = 0
        
        if (pattern and text):
            dfa = KMPAlgorithm2._dfa_array(pattern)

            while (text_index < text_length and pattern_index < pattern_length):
                # pattern_index = dfa.get(text[text_index], [0])[pattern_index]
                pattern_index = dfa[text[text_index]][pattern_index]
                text_index += 1
               
            if (pattern_index == pattern_length):
                return text_index - pattern_length
        
        return None


    def _dfa_array(pattern):
        pattern_length = len(pattern)
        x = 0

        dfa = {'A': -1, 'D': -1, 'M': -1, ' ': -1, 'I': -1, 'C': -1, 'K': -1, 'E': -1, 'W': -1, 'Z': -1, '\n': -1, 'P': -1, 'N': -1,
                 'T': -1, 'U': -1, 'S': -1, 'Y': -1, 'L': -1, 'O': -1, 'J': -1, 'B': -1, '9': -1, '7': -1, '8': -1, '-': -1, '3': -1,
                 '2': -1, '4': -1, '5': -1, 'Ę': -1, 'G': -1, 'R': -1, 'Ó': -1, '—': -1, ',': -1, 'Ł': -1, 'Ż': -1, 'Ś': -1, 'Ą': -1,
                 'Ź': -1, '!': -1, ':': -1, 'Ć': -1, '.': -1, 'H': -1, '(': -1, 'F': -1, ';': -1, 'Ń': -1, ')': -1, 'É': -1, '?': -1,
                 '…': -1, '«': -1, '»': -1, 'X': -1, 'V': -1, '*': -1, 'À': -1, '/': -1, 'Q': -1, '1': -1, 'Æ': -1, '–': -1, '0': -1,
                 '6': -1}

        for char in dfa:
            dfa[char] = [0 for i in range(pattern_length)]
 
        dfa[pattern[0]][0] = 1    

        for pattern_index in range(1, pattern_length):
            for c in dfa:                                                       # DLA KAŻDEJ LITERY ALFABETU
                dfa[c][pattern_index] = dfa[c][x]                               # PRZEJŚCIA NIE PASUJĄCE

            dfa[pattern[pattern_index]][pattern_index] = pattern_index + 1      # PRZEJŚCIA PASUJĄCE
            x = dfa[pattern[pattern_index]][x]                                  # AKTUALIZACJA STANU "PONOWNEGO URUCHAMIANIA"

        return dfa