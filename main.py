import wordlist 
import bruteforce
import nearest
import genetic_algorithm
import utils
import postprocessing
import genetic_algorithm_fixed_size
def main():
    selected_dictionary = utils.int_as_input("""
    === Please Select Your Dictionary ===
    1. 1000 most common English words
    2. Official English Scrabble Dictionary
    3. Official French Scrabble Dictionary
    4. NAPSA Zyzzyva British Scrabble List (2019)
    """, 1, 4)

    selected_method = utils.int_as_input("""
    === Please Select Method ===
    1. Brute Force
    2. Nearest Neighbor Search
    3. Genetic Algorithm
    4. Genetic Algorithm (Fixed Size Version)
    5. Genetic Algorithm (Each Size)
    """, 1, 5)
    alphabet="abcdefghijklmnopqrstuvwxyz"
    wordlistfilenames = {
        1: "words.txt",
        2: "scrabble.txt",
        3: "french_scrabble.txt",
        4: "zyzzyva.txt"
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
        combinedsolution, combinedmaxes, combinedaverages=postprocessing.start_processing(
        combinedsolution, combinedmaxes, combinedaverages, alphabet, bitfields)
        print(f"Combined solution:\nNum of words: {combinedmaxes}\n\nScore: {combinedaverages}\n\n Subsets: {combinedsolution}\n\n")
        utils.ask_for_wordlist_number(combinedsolution, words)
    elif selected_method == 3:
        num_agents=100
        iterations=1000
        best_letters = genetic_algorithm.do_genetic_algorithm(bitfields, num_agents, iterations)
        print(best_letters)
        utils.ask_for_wordlist_yn(best_letters, words)
    elif selected_method == 4:
        num_agents = 100
        iterations = 100
        size = utils.int_as_input("Choose the size of the set to be generated\n", 1, len(alphabet))
        letter_list, score = genetic_algorithm_fixed_size.do_genetic_algorithm(bitfields, num_agents, iterations, size)
        num_words=score*size
        print(letter_list)
        letter_list, num_words, score=postprocessing.start_processing(
        letter_list, num_words, score, alphabet, bitfields)
        print(f"Letter list: {letter_list}\nNum of words: {num_words}\nScore: {score}\n")
        utils.ask_for_wordlist_yn(letter_list, words)
    elif selected_method == 5:
        num_agents = 100
        iterations = 100
        letter_lists=['']*len(alphabet)
        scores=[0.0]*len(alphabet)
        num_words=[0]*len(alphabet)
        for i in range(len(letter_lists)):
            size=i+1
            letter_lists[i], scores[i]=genetic_algorithm_fixed_size.do_genetic_algorithm(bitfields, num_agents, iterations, size)
            num_words[i]=int(scores[i]*size)
        print(letter_lists)
        letter_lists, num_words, scores=postprocessing.start_processing(
        letter_lists, num_words, scores, alphabet, bitfields)
        print(f"Letter lists: {letter_lists}\nNum of words: {num_words}\nScores: {scores}\n")
        utils.ask_for_wordlist_number(letter_lists, words)
    input("Press enter to close...")

if __name__ == "__main__":
    main()

