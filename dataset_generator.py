import random as rand

four_letter_alphabet = ["A", "B", "C", "D"]
eight_letter_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H"]
twelve_letter_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]

def dataset_generator(filename, alphabet, length):
    file = open(filename, "w")

    for i in range(1, length):
        file.write(alphabet[rand.randint(0, len(alphabet) - 1)])

    file.close()




