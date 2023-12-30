#TODO
import utils
import time

def fore_minus_three_opt(subset, max, letters, bitfields):
    letterscopy=letters
    for letter in letterscopy:
        if letter in subset:
            letterscopy.remove(letter)
    for i, s_letter in enumerate(subset):
        for a_letter in letterscopy:
            subset[i]=a_letter
            count=utils.check_against_bitfields(subset, bitfields)
            if count>max:
                return fore_minus_three_opt(subset, count, letters, bitfields)
        subset[i]=s_letter
    return ''.join(subset), max

def start_processing(subsets, num_words, scores, letters, bitfields):
    print("Starting postprocessing... doing 1_opt switch")
    start_time=time.time()
    end_message=f"Time taken: {time.time()-start_time}s\n"
    if type(subsets) is list:
        for i in range(len(subsets)):
            subsets[i], num_words[i]=fore_minus_three_opt(
            list(subsets[i]), num_words[i], list(letters), bitfields)
            scores[i]=num_words[i]/(i+1)
        print(end_message)
        return subsets, num_words, scores
    subsets, num_words=fore_minus_three_opt(
    list(subsets), num_words, list(letters), bitfields)
    scores=num_words/len(subsets)
    print(end_message)
    return subsets, num_words, scores
             

