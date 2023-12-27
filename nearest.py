import utils

def find_good_letters(letters, words):
    letters=list(letters)
    subset = []
    maxes = [0]*len(letters)
    wordlists=[[]]*len(letters)
    currentletter = ' '
    for i in range(len(letters)):
        index=0
        i2=0
        for letter in letters:
            subset.append(letter)
            tempwords=utils.filter_words_by_subset(''.join(subset), words)
            if len(tempwords)>maxes[i]:
                index=i2
                maxes[i]=len(tempwords)
                currentletter=letter
                wordlists[i]=tempwords
            subset.pop()
            i2+=1
        subset.append(currentletter) 
        letters.pop(index)
    return subset, wordlists, maxes
