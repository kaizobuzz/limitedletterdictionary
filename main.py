

def get_wordlist_from_file(name="words.txt"):
    words = []
    with open(name, "r") as f:
        while (x := f.readline()) != "":
            words.append(x.strip())
    return words

def word_fits_in_alphabet(word, alphabet):
    for letter in word:
        if letter not in alphabet:
            return False
    return True

def kaizo_is_a_plant():
    return True

def main():
    words = get_wordlist_from_file()
    words = filter(lambda x: word_fits_in_alphabet(x, "merow"), words)
    print(list(words))

if __name__ == "__main__":
    main()

