from BrutalAlgorithm import BrutalAlgorithm
from KMPAlgorithm import KMPAlgorithm


if __name__ == "__main__":

    text = "ABFKROHSDSYTROVCLSJFRSCVJS"

    pattern = "SJFRSCV"
    no_pattern = "XXVXX"
    long_patern = "FFHIWJFISJOIFWOPFKSPRUYFLKSWPRUSAMFWP"

    # empty string or text
    print("Empty string:")
    print("BrutalAlgorithm:", BrutalAlgorithm.run_algorithm("", text))
    print("KMPAlgorithm:", KMPAlgorithm.run_algorithm("", text))

    print("\nEmpty text:")
    print("BrutalAlgorithm:", BrutalAlgorithm.run_algorithm(pattern, ""))
    print("KMPAlgorithm:", KMPAlgorithm.run_algorithm(pattern, ""))

    # empty string and text
    print("\nEmpty string and text:")
    print("BrutalAlgorithm:", BrutalAlgorithm.run_algorithm("", ""))
    print("KMPAlgorithm:", KMPAlgorithm.run_algorithm("", ""))

    # string = text
    print("\nString = text:")
    print("BrutalAlgorithm:", BrutalAlgorithm.run_algorithm(text, text))
    print("KMPAlgorithm:", KMPAlgorithm.run_algorithm(text, text))

    # string > text
    print("\nString > text:")
    print("BrutalAlgorithm:", BrutalAlgorithm.run_algorithm(long_patern, text))
    print("KMPAlgorithm:", KMPAlgorithm.run_algorithm(long_patern, text))

    # string not in text
    print("\nString not in text:")
    print("BrutalAlgorithm:", BrutalAlgorithm.run_algorithm(no_pattern, text))
    print("KMPAlgorithm:", KMPAlgorithm.run_algorithm(no_pattern, text))

    # predefined string-text pairs
    pairs = [("KOMPUTER", "SGEJCEKOMPUTERDWOCJW"), ("AABA", "AABAACAADAABAABA"), 
             ("AAAAA", "AAAAAAAAAAAAAAAAAA"), ("AAAAB", "AAAAAAAAAAAAAAAAAB"), 
             ("FAA", "AABCCAADDEE"), (pattern, text)]

    print("\nPredefined string-text pairs:")
    for pair in pairs:
        print("BrutalAlgorithm:", pair[0], pair[1], BrutalAlgorithm.run_algorithm(pair[0], pair[1]))
        print("KMPAlgorithm:", pair[0], pair[1], KMPAlgorithm.run_algorithm(pair[0], pair[1]))
            