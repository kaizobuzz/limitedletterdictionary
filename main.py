import wordlist 
import bruteforce
import nearest
import genetic_algorithm
import utils
import postprocessing
import time
import genetic_algorithm_fixed_size
def main():
    selected_dictionary = utils.int_as_input("""
    === Please Select Your Dictionary ===
    1. 1000 most common English words
    2. Official English Scrabble Dictionary
    3. Official French Scrabble Dictionary
    """, 1, 3)

    selected_method = utils.int_as_input("""
    === Please Select Method ===
    1. Brute Force
    2. Nearest Neighbor Search
    3. Genetic Algorithm
    4. Genetic Algorithm (Fixed Size Version)
    """, 1, 4)
    alphabet="abcdefghijklmnopqrstuvwxyz"
    wordlistfilenames = {
        1: "words.txt",
        2: "scrabble.txt",
        3: "french_scrabble.txt"
    }
    words = wordlist.get_wordlist_from_file(name=wordlistfilenames[selected_dictionary])
    bitfields = wordlist.create_bitfields(words)
    if selected_method == 1:
        solution, maxes, averages = bruteforce.find_optimal_letters(alphabet, bitfields)
        print(f"Num of words: {maxes}\n\nScore: {averages}\n\nSolutions: {solution}")
        utils.ask_for_wordlist_number(solution, words)
    elif selected_method == 2:
        solution, maxes, averages=nearest.find_good_letters(alphabet, bitfields)
        #print(solutionwords, "\n") 
        print(f"Forwards solution:\nNum of words: {maxes}\n\nScore: {averages}\n\nLetter Order: {solution}\n")
        solutionbw, maxesbw, averagesbw=nearest.find_good_letters_reverse(alphabet, bitfields)
        print(f"Backwards solution:\nNum of words: {maxesbw}\n\nScore: {averagesbw}\n\nLetter Order: {solutionbw}\n")
        combinedsolution=['']*26
        combinedmaxes=[0]*26
        combinedaverages=[0.0]*26
        for i in range(len(maxes)):
            if maxes[i]>=maxesbw[i]:
                combinedmaxes[i]=maxes[i]
                combinedaverages[i]=averages[i]
                combinedsolution[i]=''.join(solution)[:i+1:]
            else:
                combinedmaxes[i]=maxesbw[i]
                combinedaverages[i]=averagesbw[i]
                combinedsolution[i]=''.join(solutionbw)[:i+1:]
        print(f"Combined solution:\nNum of words: {combinedmaxes}\n\nScore: {combinedaverages}\n\n Subsets: {combinedsolution}\n\n")
        print("Starting postprocessing... doing 1_opt switch\n")
        start_time=time.time()
        for i in range(len(combinedsolution)):
            combinedsolution[i], combinedmaxes[i]=postprocessing.fore_minus_three_opt(
            list(combinedsolution[i]), combinedmaxes[i], list(alphabet), bitfields)
            combinedaverages[i]=combinedmaxes[i]/(i+1)
        print(f"Time taken: {time.time()-start_time}s\n")
        print(f"Combined solution:\nNum of words: {combinedmaxes}\n\nScore: {combinedaverages}\n\n Subsets: {combinedsolution}\n\n")
        utils.ask_for_wordlist_number(combinedsolution, words)
    elif selected_method == 3:
        num_agents=100
        iterations=10000
        best_letters = genetic_algorithm.do_genetic_algorithm(bitfields, num_agents, iterations)
        print(best_letters)
        utils.ask_for_wordlist_yn(best_letters, words)
    elif selected_method == 4:
        num_agents = 100
        iterations = 100
        size = utils.int_as_input("Choose the size of the set to be generated\n", 1, 26)
        letter_list, score = genetic_algorithm_fixed_size.do_genetic_algorithm(bitfields, num_agents, iterations, size)
        num_words=score*size
        print(letter_list)
        print("Starting postprocessing... doing 1_opt switch")
        start_time=time.time()
        letter_list, num_words=postprocessing.fore_minus_three_opt(
                list(letter_list), num_words, list(alphabet), bitfields)
        print(f"Time taken: {time.time()-start_time}s\n")
        print(f"Letter list: {letter_list}\nNum of words: {num_words}\nScore: {score}\n")
        utils.ask_for_wordlist_yn(letter_list, words)
    input("Press enter to close...")

if __name__ == "__main__":
    main()

