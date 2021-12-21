import matplotlib.pyplot as plt
from random import randint, choice

import time
import gc

class Utils():
    def __init__(self):
        pass

    @staticmethod
    def _get_alphabet(text):
        alphabet = {char: -1 for char in text}

        return alphabet


    def _clear_words(words_list):
        illegal_chars = ['\n', ",", ".", "?", "!", ";", ":", "-", "–", "—", "/", "(", ")",
                        "…", "»", "«", "*", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        table = []

        for word in words_list:
            for char in word:
                if (char in illegal_chars):
                    word = word.replace(char, "")
            
            if (word != ""):
                table.append(word)

        return table



    def _generate_text_of_random_words(number_of_elements, max_word_length=15):
        # alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
        #             "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
        #             "U", "W", "V", "X", "Y", "Z"]
        alphabet = ["A", "B"]

        text = ""

        for i in range(number_of_elements):
            word_length = randint(1, max_word_length)
            word = ""

            for j in range(word_length):
                word += choice(alphabet)
            
            text += word + " "

        return text


    def _generate_text_from_file(file_name):
        with open(file_name, encoding='utf8') as file:
            text = file.read().upper()

        return text


    def _generate_words_list_from_text(text):
        words_list = text.split()
        # words_list = Utils._clear_words(words_list)

        return words_list


    def _draw_plot(algorithm_name, xpoints, ypoints):
        figure1 = plt.figure()
        plt.plot(xpoints, ypoints, marker='o')
        plt.title(algorithm_name)
        plt.xlabel("Number of elements")
        plt.ylabel("Process time [s]")
        plt.savefig(algorithm_name + ".png")
        # plt.show()
        plt.close(figure1)

        # plt.semilogy(xpoints, ypoints, marker='o', label=algorithm_name)
        plt.plot(xpoints, ypoints, marker='o', label=algorithm_name)
        plt.title("All algorithms")
        plt.xlabel("Number of elements")
        plt.ylabel("Process time [s]")
        plt.legend(loc="upper left")
        plt.savefig("All algorithms.png")
        # plt.show()


    def _measure_time(algorithm, text, pattern):
        gc_old = gc.isenabled()
        gc.disable()

        start = time.process_time()
        found_index = algorithm.run_algorithm(pattern, text)
        stop = time.process_time()

        if (gc_old): 
            gc.enable()

        return stop - start


    @staticmethod
    def start_measurements(algorithm, file_name, number_of_elements_list, shift=0):
        text = Utils._generate_text_from_file(file_name)
        words_list = Utils._generate_words_list_from_text(text)
        algorithm_name = str(algorithm())
        ypoints = []

        print(algorithm_name, "\n--------------")

        for number_of_elements in number_of_elements_list:
            process_time = 0
            for pattern in words_list[shift:shift + number_of_elements]:
                process_time += Utils._measure_time(algorithm, text, pattern)
            
            ypoints.append(process_time)

            print("PROCESS TIME:", format(process_time, '.10f'), "FOR", number_of_elements, "ELEMENTS")

        Utils._draw_plot(algorithm_name, number_of_elements_list, ypoints)
