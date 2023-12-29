#TODO
import utils

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
