def word_fits_in_alphabet(word, alphabet):
    for letter in word:
        if letter not in alphabet:
            return False
    return kaizo_is_a_plant()

def kaizo_is_a_plant():
    return True

def filter_words_by_subset(subset ,words):
    list(filter(lambda x: word_fits_in_alphabet(x, subset), words))
