import wordlist 
import bruteforce
import nearest
import genetic_algorithm

def main():
    selected_dictionary = int(input("""
    === Please Select Your Dictionary ===
    1. 1000 most common English words
    2. Official English Scrabble Dictionary
    3. Official French Scrabble Dictionary
    """))

    selected_method = int(input("""
    === Please Select Method ===
    1. Brute Force
    2. Nearest Neighbor Search
    3. Genetic Algorithm
    """))
    alphabet="abcdefghijklmnopqrstuvwxyz"
    wordlistfilenames = {
        1: "words.txt",
        2: "scrabble.txt",
        3: "french_scrabble.txt"
    }
    words = wordlist.get_wordlist_from_file(name=wordlistfilenames[selected_dictionary])

    if selected_method == 1:
        solution, solutionwords = bruteforce.find_optimal_letters(alphabet, words)
        print(solution, "\n\n", solutionwords)
    elif selected_method == 2:
        solution, solutionwords, maxes, averages=nearest.find_good_letters(alphabet, words)
        #print(solutionwords, "\n") 
        print(maxes, "\n\n", averages, "\n\n", solution)
    elif selected_method == 3:
        num_agents=100
        iterations=10000
        best_letters = genetic_algorithm.do_genetic_algorithm(words, num_agents, iterations)
        print(best_letters)

    input("Press enter to close...")

if __name__ == "__main__":
    main()

