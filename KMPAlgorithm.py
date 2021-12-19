class KMPAlgorithm:
    def __init__(self):
        pass


    def __str__(self):
        return "KMPAlgorithm"


    @staticmethod
    def run_algorithm(pattern, text):
        m = len(pattern)
        n = len(text)
        i = 0
        j = 0
        
        if (pattern and text):
            dfa = KMPAlgorithm._dfa_array(pattern)

            while (i < n and j < m):
                # j = dfa.get(text[i], [0])[j]
                if (text[i] in dfa):
                    j = dfa[text[i]][j]
                else:
                    j = 0

                i += 1
               
            if (j == m):
                return i - m
        
        return None


    def _dfa_array(pattern):
        m = len(pattern)
        dfa = {}
        x = 0

        for char in pattern:
            if (char not in dfa):
                dfa[char] = [0 for i in range(m)]
 
        dfa[pattern[0]][0] = 1    

        for j in range(1, m):
            for c in dfa:                       # DLA KAŻDEJ LITERY ALFABETU
                dfa[c][j] = dfa[c][x]           # PRZEJŚCIA NIE PASUJĄCE
            dfa[pattern[j]][j] = j + 1          # PRZEJŚCIA PASUJĄCE
            x = dfa[pattern[j]][x]              # AKTUALIZACJA STANU "PONOWNEGO URUCHAMIANIA"

        return dfa