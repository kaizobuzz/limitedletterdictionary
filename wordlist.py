
def get_wordlist_from_file(name="words.txt"):
    words = []
    with open(name, "r") as f:
        while (x := f.readline()) != "":
            words.append(x.strip())
        return words

def deduplicate_word_list(words):
    new_words = {}
    for word in words:
        if simplify_word(word) in new_words:
            new_words[simplify_word(word)] += 1
        else:
            new_words[simplify_word(word)] = 1
    return new_words

def simplify_word(word):
    return "".join(sorted("".join(set(word))))
