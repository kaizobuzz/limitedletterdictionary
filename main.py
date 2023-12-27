import wordlist 
import bruteforce
import nearest
import genetic_algorithm

def main():
    selected_method = int(input("""
    === Please Select Method ===
    1. Brute Force
    2. Nearest Neighbor Search
    3. Genetic Algorithm
    """))
    alphabet="abcdefghijklmnopqrstuvwxyz"
    words = wordlist.get_wordlist_from_file()

    if selected_method == 1:
        solution, solutionwords = bruteforce.find_optimal_letters(alphabet, words)
        print(solution, "\n\n", solutionwords)
    elif selected_method == 2:
        solution, solutionwords, maxes=nearest.find_good_letters(alphabet, words)
        print(solution, "\n", maxes, "\n\n", solutionwords)
    elif selected_method == 3:
        best_letters = genetic_algorithm.do_genetic_algorithm(words, 1000, 1000)
        print(best_letters)

    input("Press enter to close...")

if __name__ == "__main__":
    main()

