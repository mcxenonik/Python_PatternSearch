from BrutalAlgorithm import BrutalAlgorithm
from BrutalAlgorithm2 import BrutalAlgorithm2
from KMPAlgorithm import KMPAlgorithm
from KMPAlgorithm2 import KMPAlgorithm2
from KMPAlgorithm3 import KMPAlgorithm3
from BMAlgorithm import BMAlgorithm
from BMAlgorithm2 import BMAlgorithm2
from RKAlgorithm import RKAlgorithm
from PythonAlgorithm import PythonAlgorithm
from Utils import Utils


if __name__ == "__main__":

    text = "ABFKROHSDSYTROVCLSJFRSCVJS"

    pattern = "SJFRSCV"
    no_pattern = "XXVXX"
    long_patern = "FFHIWJFISJOIFWOPFKSPRUYFLKSWPRUSAMFWP"

    # empty string
    print("=====================================================================")
    print("Empty string:\n---")
    print("BrutalAlgorithm: ", BrutalAlgorithm.run_algorithm("", text))
    print("BrutalAlgorithm2:", BrutalAlgorithm2.run_algorithm("", text))
    print("KMPAlgorithm:    ", KMPAlgorithm.run_algorithm("", text))
    print("KMPAlgorithm2:   ", KMPAlgorithm2.run_algorithm("", text))
    print("KMPAlgorithm3:   ", KMPAlgorithm3.run_algorithm("", text))
    print("BMAlgorithm:     ", BMAlgorithm.run_algorithm("", text))
    print("BMAlgorithm2:    ", BMAlgorithm2.run_algorithm("", text))
    print("RKAlgorithm:     ", RKAlgorithm.run_algorithm("", text))
    print("PythonAlgorithm: ", PythonAlgorithm.run_algorithm("", text))

    # empty text
    print("=====================================================================")
    print("\nEmpty text:\n---")
    print("BrutalAlgorithm: ", BrutalAlgorithm.run_algorithm(pattern, ""))
    print("BrutalAlgorithm2:", BrutalAlgorithm2.run_algorithm(pattern, ""))
    print("KMPAlgorithm:    ", KMPAlgorithm.run_algorithm(pattern, ""))
    print("KMPAlgorithm2:   ", KMPAlgorithm2.run_algorithm(pattern, ""))
    print("KMPAlgorithm3:   ", KMPAlgorithm3.run_algorithm(pattern, ""))
    print("BMAlgorithm:     ", BMAlgorithm.run_algorithm(pattern, ""))
    print("BMAlgorithm2:    ", BMAlgorithm2.run_algorithm(pattern, ""))
    print("RKAlgorithm:     ", RKAlgorithm.run_algorithm(pattern, ""))
    print("PythonAlgorithm: ", PythonAlgorithm.run_algorithm(pattern, ""))

    # empty string and text
    print("=====================================================================")
    print("\nEmpty string and text:\n---")
    print("BrutalAlgorithm: ", BrutalAlgorithm.run_algorithm("", ""))
    print("BrutalAlgorithm2:", BrutalAlgorithm2.run_algorithm("", ""))
    print("KMPAlgorithm:    ", KMPAlgorithm.run_algorithm("", ""))
    print("KMPAlgorithm2:   ", KMPAlgorithm2.run_algorithm("", ""))
    print("KMPAlgorithm3:   ", KMPAlgorithm3.run_algorithm("", ""))
    print("BMAlgorithm:     ", BMAlgorithm.run_algorithm("", ""))
    print("BMAlgorithm2:    ", BMAlgorithm2.run_algorithm("", ""))
    print("RKAlgorithm:     ", RKAlgorithm.run_algorithm("", ""))
    print("PythonAlgorithm: ", PythonAlgorithm.run_algorithm("", ""))

    # string = text
    print("=====================================================================")
    print("\nString = text:\n---")
    print("BrutalAlgorithm: ", BrutalAlgorithm.run_algorithm(text, text))
    print("BrutalAlgorithm2:", BrutalAlgorithm2.run_algorithm(text, text))
    print("KMPAlgorithm:    ", KMPAlgorithm.run_algorithm(text, text))
    print("KMPAlgorithm2:   ", KMPAlgorithm2.run_algorithm(text, text))
    print("KMPAlgorithm3:   ", KMPAlgorithm3.run_algorithm(text, text))
    print("BMAlgorithm:     ", BMAlgorithm.run_algorithm(text, text))
    print("BMAlgorithm2:    ", BMAlgorithm2.run_algorithm(text, text))
    print("RKAlgorithm:     ", RKAlgorithm.run_algorithm(text, text))
    print("PythonAlgorithm: ", PythonAlgorithm.run_algorithm(text, text))

    # string > text
    print("=====================================================================")
    print("\nString > text:\n---")
    print("BrutalAlgorithm: ", BrutalAlgorithm.run_algorithm(long_patern, text))
    print("BrutalAlgorithm2:", BrutalAlgorithm2.run_algorithm(long_patern, text))
    print("KMPAlgorithm:    ", KMPAlgorithm.run_algorithm(long_patern, text))
    print("KMPAlgorithm2:   ", KMPAlgorithm2.run_algorithm(long_patern, text))
    print("KMPAlgorithm3:   ", KMPAlgorithm3.run_algorithm(long_patern, text))
    print("BMAlgorithm:     ", BMAlgorithm.run_algorithm(long_patern, text))
    print("BMAlgorithm2:    ", BMAlgorithm2.run_algorithm(long_patern, text))
    print("RKAlgorithm:     ", RKAlgorithm.run_algorithm(long_patern, text))
    print("PythonAlgorithm: ", PythonAlgorithm.run_algorithm(long_patern, text))

    # string in text
    print("=====================================================================")
    print("\nString in text:\n---")
    print("BrutalAlgorithm: ", BrutalAlgorithm.run_algorithm(pattern, text))
    print("BrutalAlgorithm2:", BrutalAlgorithm2.run_algorithm(pattern, text))
    print("KMPAlgorithm:    ", KMPAlgorithm.run_algorithm(pattern, text))
    print("KMPAlgorithm2:   ", KMPAlgorithm2.run_algorithm(pattern, text))
    print("KMPAlgorithm3:   ", KMPAlgorithm3.run_algorithm(pattern, text))
    print("BMAlgorithm:     ", BMAlgorithm.run_algorithm(pattern, text))
    print("BMAlgorithm2:    ", BMAlgorithm2.run_algorithm(pattern, text))
    print("RKAlgorithm:     ", RKAlgorithm.run_algorithm(pattern, text))
    print("PythonAlgorithm: ", PythonAlgorithm.run_algorithm(pattern, text))

    # string not in text
    print("=====================================================================")
    print("\nString not in text:\n---")
    print("BrutalAlgorithm: ", BrutalAlgorithm.run_algorithm(no_pattern, text))
    print("BrutalAlgorithm2:", BrutalAlgorithm2.run_algorithm(no_pattern, text))
    print("KMPAlgorithm:    ", KMPAlgorithm.run_algorithm(no_pattern, text))
    print("KMPAlgorithm2:   ", KMPAlgorithm2.run_algorithm(no_pattern, text))
    print("KMPAlgorithm3:   ", KMPAlgorithm3.run_algorithm(no_pattern, text))
    print("BMAlgorithm:     ", BMAlgorithm.run_algorithm(no_pattern, text))
    print("BMAlgorithm2:    ", BMAlgorithm2.run_algorithm(no_pattern, text))
    print("RKAlgorithm:     ", RKAlgorithm.run_algorithm(no_pattern, text))
    print("PythonAlgorithm: ", PythonAlgorithm.run_algorithm(no_pattern, text))

    # predefined pairs
    print("=====================================================================")
    print("\nPredefined pairs:\n---")
    pairs = [("KOMPUTER", "SGEJCEKOMPUTERDWOCJW"), ("AABA", "AABAACAADAABAABA"), 
             ("AAAAA", "AAAAAAAAAAAAAAAAAA"), ("AAAAB", "AAAAAAAAAAAAAAAAAB"), 
             ("FAA", "AABCCAADDEE"), ("ABAAB", "AAAAAABAABAAB")]

    for pair in pairs:
        print("BrutalAlgorithm: ", pair[0], pair[1], BrutalAlgorithm.run_algorithm(pair[0], pair[1]), "| PYTHON FIND:", pair[1].find(pair[0]))
        print("BrutalAlgorithm2:", pair[0], pair[1], BrutalAlgorithm2.run_algorithm(pair[0], pair[1]), "| PYTHON FIND:", pair[1].find(pair[0]))
        print("KMPAlgorithm:    ", pair[0], pair[1], KMPAlgorithm.run_algorithm(pair[0], pair[1]), "| PYTHON FIND:", pair[1].find(pair[0]))
        print("KMPAlgorithm2:   ", pair[0], pair[1], KMPAlgorithm2.run_algorithm(pair[0], pair[1]), "| PYTHON FIND:", pair[1].find(pair[0]))
        print("KMPAlgorithm3:   ", pair[0], pair[1], KMPAlgorithm3.run_algorithm(pair[0], pair[1]), "| PYTHON FIND:", pair[1].find(pair[0]))
        print("BMAlgorithm:     ", pair[0], pair[1], BMAlgorithm.run_algorithm(pair[0], pair[1]), "| PYTHON FIND:", pair[1].find(pair[0]))
        print("BMAlgorithm2:    ", pair[0], pair[1], BMAlgorithm2.run_algorithm(pair[0], pair[1]), "| PYTHON FIND:", pair[1].find(pair[0]))
        print("RKAlgorithm:     ", pair[0], pair[1], RKAlgorithm.run_algorithm(pair[0], pair[1]), "| PYTHON FIND:", pair[1].find(pair[0]))
        print("PythonAlgorithm: ", pair[0], pair[1], PythonAlgorithm.run_algorithm(pair[0], pair[1]), "| PYTHON FIND:", pair[1].find(pair[0]))
        print("---")
            

    # Predefined text
    print("=====================================================================")
    print("\nPredefined text:\n---")
    text = "SGFIEWFSMO MSDO SPOWEADLPFASK,;A3-0PC KPSE 304T-RW, 3A/AS -3RALS.C -3RSA7CAS LEWRO3AD 3A/AS ,AD2P1 AS ,23QR-A DF3A/AS,.ADLPFASK,;A3-"
    words_list = ["SGFIEWFSMO", "3A/AS", "-3RSA7CAS", ",AD2P1", "ADLPFASK,;A3-"]
    print(text)
    print("---")

    for pattern in words_list:
        print("BrutalAlgorithm: ", pattern, BrutalAlgorithm.run_algorithm(pattern, text), "| PYTHON FIND:", text.find(pattern))
        print("BrutalAlgorithm2:", pattern, BrutalAlgorithm2.run_algorithm(pattern, text), "| PYTHON FIND:", text.find(pattern))
        print("KMPAlgorithm:    ", pattern, KMPAlgorithm.run_algorithm(pattern, text), "| PYTHON FIND:", text.find(pattern))
        print("KMPAlgorithm2:   ", pattern, KMPAlgorithm2.run_algorithm(pattern, text), "| PYTHON FIND:", text.find(pattern))
        print("KMPAlgorithm3:   ", pattern, KMPAlgorithm3.run_algorithm(pattern, text), "| PYTHON FIND:", text.find(pattern))
        print("BMAlgorithm:     ", pattern, BMAlgorithm.run_algorithm(pattern, text), "| PYTHON FIND:", text.find(pattern))
        print("BMAlgorithm2:    ", pattern, BMAlgorithm2.run_algorithm(pattern, text), "| PYTHON FIND:", text.find(pattern))
        print("RKAlgorithm:     ", pattern, RKAlgorithm.run_algorithm(pattern, text), "| PYTHON FIND:", text.find(pattern))
        print("PythonAlgorithm: ", pattern, PythonAlgorithm.run_algorithm(pattern, text), "| PYTHON FIND:", text.find(pattern))
        print("---")


    # random words
    print("=====================================================================")
    print("\nRandom words:\n---")
    text = Utils._generate_text_of_random_words(10, 15)
    words_list = Utils._generate_words_list_from_text(text)
    print(text)
    print("---")

    for pattern in words_list[:5]:
        print("BrutalAlgorithm: ", pattern, BrutalAlgorithm.run_algorithm(pattern, text), "| PYTHON FIND:", text.find(pattern))
        print("BrutalAlgorithm2:", pattern, BrutalAlgorithm2.run_algorithm(pattern, text), "| PYTHON FIND:", text.find(pattern))
        print("KMPAlgorithm:    ", pattern, KMPAlgorithm.run_algorithm(pattern, text), "| PYTHON FIND:", text.find(pattern))
        print("KMPAlgorithm2:   ", pattern, KMPAlgorithm2.run_algorithm(pattern, text), "| PYTHON FIND:", text.find(pattern))
        print("KMPAlgorithm3:   ", pattern, KMPAlgorithm3.run_algorithm(pattern, text), "| PYTHON FIND:", text.find(pattern))
        print("BMAlgorithm:     ", pattern, BMAlgorithm.run_algorithm(pattern, text), "| PYTHON FIND:", text.find(pattern))
        print("BMAlgorithm2:    ", pattern, BMAlgorithm2.run_algorithm(pattern, text), "| PYTHON FIND:", text.find(pattern))
        print("RKAlgorithm:     ", pattern, RKAlgorithm.run_algorithm(pattern, text), "| PYTHON FIND:", text.find(pattern))
        print("PythonAlgorithm: ", pattern, PythonAlgorithm.run_algorithm(pattern, text), "| PYTHON FIND:", text.find(pattern))
        print("---")

    # text = Utils._generate_text_from_file("pan-tadeusz.txt")
    # print(Utils._get_alphabet(text))