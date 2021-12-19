from BrutalAlgorithm import BrutalAlgorithm
from BrutalAlgorithm2 import BrutalAlgorithm2
from KMPAlgorithm import KMPAlgorithm
from Utils import Utils

def run(input_file_name, number_of_elements_list):
    Utils.start_measurements(BrutalAlgorithm, input_file_name, number_of_elements_list)

    Utils.start_measurements(BrutalAlgorithm2, input_file_name, number_of_elements_list)

    Utils.start_measurements(KMPAlgorithm, input_file_name, number_of_elements_list)


if __name__ == "__main__":
    input_file_name = "pan-tadeusz.txt"
    # number_of_elements_list = [n for n in range(1000, 68336, 5000)]            # MAX 68336
    number_of_elements_list = [n for n in range(100, 2001, 100)]

    run(input_file_name, number_of_elements_list)
