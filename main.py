import wordlist 
import bruteforce

def main():
    words = wordlist.get_wordlist_from_file()
    #words = filter(lambda x: word_fits_in_alphabet(x, "merow"), words)
    #print(list(words))
    solution, solutionwords=bruteforce.find_optimal_letters("abcdefghijklmnopqrstuvwxyz", words)     
    print(solution, "\n\n")
    print(solutionwords)
    #print(wordlist.deduplicate_word_list(wordlist.get_wordlist_from_file()))

if __name__ == "__main__":
    main()

