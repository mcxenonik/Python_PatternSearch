class KMPAlgorithm3:
    def __init__(self):
        pass


    def __str__(self):
        return "KMP_Algorithm_3"


    @staticmethod
    def run_algorithm(pattern, text):
        M = len(pattern)
        N = len(text)

        results = []
    
        # create lps[] that will hold the longest prefix suffix 
        # values for pattern
        lps = [0]*M
        j = 0 # index for pat[]
    
        if (pattern and text):
            # Preprocess the pattern (calculate lps[] array)
            KMPAlgorithm3.computeLPSArray(pattern, M, lps)
        
            i = 0 # index for txt[]
            while i < N:
                if pattern[j] == text[i]:
                    i += 1
                    j += 1
        
                if j == M:
                    # return i - j
                    results.append(i - j)
                    i -= j
                    j = 0
                    i += 1
                    # j = lps[j-1]
        
                # mismatch after j matches
                elif i < N and pattern[j] != text[i]:
                    # Do not match lps[0..lps[j-1]] characters,
                    # they will match anyway
                    if j != 0:
                        j = lps[j-1]
                    else:
                        i += 1

        if (results):
            return results
        else:
            return None


    @staticmethod
    def run_algorithm2(pattern, text):
        M = len(pattern)
        N = len(text)
    
        # create lps[] that will hold the longest prefix suffix 
        # values for pattern
        lps = [0]*M
        j = 0 # index for pat[]
    
        # Preprocess the pattern (calculate lps[] array)
        KMPAlgorithm3.computeLPSArray(pattern, M, lps)
    
        i = 0 # index for txt[]
        while i < N:
            if pattern[j] == text[i]:
                i += 1
                j += 1
    
            if j == M:
                return i - j
                # j = lps[j-1]
    
            # mismatch after j matches
            elif i < N and pattern[j] != text[i]:
                # Do not match lps[0..lps[j-1]] characters,
                # they will match anyway
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1


    def computeLPSArray(pat, M, lps):
        len = 0 # length of the previous longest prefix suffix
    
        lps[0] # lps[0] is always 0
        i = 1
    
        # the loop calculates lps[i] for i = 1 to M-1
        while i < M:
            if pat[i]== pat[len]:
                len += 1
                lps[i] = len
                i += 1
            else:
                # This is tricky. Consider the example.
                # AAACAAAA and i = 7. The idea is similar 
                # to search step.
                if len != 0:
                    len = lps[len-1]
    
                    # Also, note that we do not increment i here
                else:
                    lps[i] = 0
                    i += 1