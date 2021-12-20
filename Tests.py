from BrutalAlgorithm import BrutalAlgorithm
from BrutalAlgorithm2 import BrutalAlgorithm2
from KMPAlgorithm import KMPAlgorithm
from BMAlgorithm import BMAlgorithm
from BMAlgorithm2 import BMAlgorithm2


if __name__ == "__main__":

    text = "ABFKROHSDSYTROVCLSJFRSCVJS"

    pattern = "SJFRSCV"
    no_pattern = "XXVXX"
    long_patern = "FFHIWJFISJOIFWOPFKSPRUYFLKSWPRUSAMFWP"

    # empty string or text
    print("Empty string:")
    print("BrutalAlgorithm:", BrutalAlgorithm.run_algorithm("", text))
    print("BrutalAlgorithm2:", BrutalAlgorithm2.run_algorithm("", text))
    print("KMPAlgorithm:", KMPAlgorithm.run_algorithm("", text))
    print("BMAlgorithm:", BMAlgorithm.run_algorithm("", text))
    print("BMAlgorithm2:", BMAlgorithm2.run_algorithm("", text))

    print("\nEmpty text:")
    print("BrutalAlgorithm:", BrutalAlgorithm.run_algorithm(pattern, ""))
    print("BrutalAlgorithm2:", BrutalAlgorithm2.run_algorithm(pattern, ""))
    print("KMPAlgorithm:", KMPAlgorithm.run_algorithm(pattern, ""))
    print("BMAlgorithm:", BMAlgorithm.run_algorithm(pattern, ""))
    print("BMAlgorithm2:", BMAlgorithm2.run_algorithm(pattern, ""))

    # empty string and text
    print("\nEmpty string and text:")
    print("BrutalAlgorithm:", BrutalAlgorithm.run_algorithm("", ""))
    print("BrutalAlgorithm2:", BrutalAlgorithm2.run_algorithm("", ""))
    print("KMPAlgorithm:", KMPAlgorithm.run_algorithm("", ""))
    print("BMAlgorithm:", BMAlgorithm.run_algorithm("", ""))
    print("BMAlgorithm2:", BMAlgorithm2.run_algorithm("", ""))

    # string = text
    print("\nString = text:")
    print("BrutalAlgorithm:", BrutalAlgorithm.run_algorithm(text, text))
    print("BrutalAlgorithm2:", BrutalAlgorithm2.run_algorithm(text, text))
    print("KMPAlgorithm:", KMPAlgorithm.run_algorithm(text, text))
    print("BMAlgorithm:", BMAlgorithm.run_algorithm(text, text))
    print("BMAlgorithm2:", BMAlgorithm2.run_algorithm(text, text))

    # string > text
    print("\nString > text:")
    print("BrutalAlgorithm:", BrutalAlgorithm.run_algorithm(long_patern, text))
    print("BrutalAlgorithm2:", BrutalAlgorithm2.run_algorithm(long_patern, text))
    print("KMPAlgorithm:", KMPAlgorithm.run_algorithm(long_patern, text))
    print("BMAlgorithm:", BMAlgorithm.run_algorithm(long_patern, text))
    print("BMAlgorithm2:", BMAlgorithm2.run_algorithm(long_patern, text))

    # string in text
    print("\nString in text:")
    print("BrutalAlgorithm:", BrutalAlgorithm.run_algorithm(pattern, text))
    print("BrutalAlgorithm2:", BrutalAlgorithm2.run_algorithm(pattern, text))
    print("KMPAlgorithm:", KMPAlgorithm.run_algorithm(pattern, text))
    print("BMAlgorithm:", BMAlgorithm.run_algorithm(pattern, text))
    print("BMAlgorithm2:", BMAlgorithm2.run_algorithm(pattern, text))

    # string not in text
    print("\nString not in text:")
    print("BrutalAlgorithm:", BrutalAlgorithm.run_algorithm(no_pattern, text))
    print("BrutalAlgorithm2:", BrutalAlgorithm2.run_algorithm(no_pattern, text))
    print("KMPAlgorithm:", KMPAlgorithm.run_algorithm(no_pattern, text))
    print("BMAlgorithm:", BMAlgorithm.run_algorithm(no_pattern, text))
    print("BMAlgorithm2:", BMAlgorithm2.run_algorithm(no_pattern, text))

    # predefined string-text pairs
    pairs = [("KOMPUTER", "SGEJCEKOMPUTERDWOCJW"), ("AABA", "AABAACAADAABAABA"), 
             ("AAAAA", "AAAAAAAAAAAAAAAAAA"), ("AAAAB", "AAAAAAAAAAAAAAAAAB"), 
             ("FAA", "AABCCAADDEE"), (pattern, text)]

    print("\nPredefined string-text pairs:")
    for pair in pairs:
        print("BrutalAlgorithm:", pair[0], pair[1], BrutalAlgorithm.run_algorithm(pair[0], pair[1]))
        print("BrutalAlgorithm2:", pair[0], pair[1], BrutalAlgorithm2.run_algorithm(pair[0], pair[1]))
        print("KMPAlgorithm:", pair[0], pair[1], KMPAlgorithm.run_algorithm(pair[0], pair[1]))
        print("BMAlgorithm:", pair[0], pair[1], BMAlgorithm.run_algorithm(pair[0], pair[1]))
        print("BMAlgorithm2:", pair[0], pair[1], BMAlgorithm2.run_algorithm(pair[0], pair[1]))
        print("---")
            