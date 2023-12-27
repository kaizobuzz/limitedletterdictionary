

def get_wordlist_from_file(name="words.txt"):
    words = []
    with open(name, "r") as f:
        while (x := f.readline()) != "":
            words.append(x)
    return words

