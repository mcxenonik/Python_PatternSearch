from BrutalAlgorithm import BrutalAlgorithm
from BrutalAlgorithm2 import BrutalAlgorithm2
from KMPAlgorithm import KMPAlgorithm
from KMPAlgorithm2 import KMPAlgorithm2
from BMAlgorithm import BMAlgorithm
from BMAlgorithm2 import BMAlgorithm2
from RKAlgorithm import RKAlgorithm
from Utils import Utils

def run(input_file_name, number_of_elements_list):
    Utils.start_measurements(BrutalAlgorithm, input_file_name, number_of_elements_list)

    Utils.start_measurements(BrutalAlgorithm2, input_file_name, number_of_elements_list)

    Utils.start_measurements(KMPAlgorithm, input_file_name, number_of_elements_list)

    Utils.start_measurements(RKAlgorithm, input_file_name, number_of_elements_list)

    Utils.start_measurements(BMAlgorithm, input_file_name, number_of_elements_list)

    Utils.start_measurements(BMAlgorithm2, input_file_name, number_of_elements_list)

    Utils.start_measurements(KMPAlgorithm2, input_file_name, number_of_elements_list)


if __name__ == "__main__":
    input_file_name = "pan-tadeusz.txt"
    # number_of_elements_list = [n for n in range(1000, 68336, 5000)]            # MAX 68336
    # number_of_elements_list = [n for n in range(100, 5001, 100)]
    number_of_elements_list = [n for n in range(100, 2001, 100)]
    # number_of_elements_list = [n for n in range(10, 15, 10)]

    run(input_file_name, number_of_elements_list)
