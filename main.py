import wordlist 
import bruteforce
import nearest

def main():
    alphabet="abcdefghijklmnopqrstuvwxyz"
    words = wordlist.get_wordlist_from_file()
    #words = filter(lambda x: word_fits_in_alphabet(x, "merow"), words)
    #print(list(words))
    solution, solutionwords, maxes=nearest.find_good_letters(alphabet, words)
    print(solution, "\n", maxes, "\n\n", solutionwords)
    input("nearest neighbour heuristic finished, press enter to start thingy after...")
    solution, solutionwords=bruteforce.find_optimal_letters(alphabet, words)     
    print(solution, "\n\n")
    print(solutionwords)
    #print(wordlist.deduplicate_word_list(wordlist.get_wordlist_from_file()))

if __name__ == "__main__":
    main()

