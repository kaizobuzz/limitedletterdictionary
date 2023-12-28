import utils
import time

def find_good_letters(letters, words):
    start_time=time.time()
    letters=list(letters)
    subset = []
    maxes = [0]*len(letters)
    wordlists=[[]]*len(letters)
    currentletter = ' '
    for i in range(len(letters)):
        index=0
        for i2, letter in enumerate(letters):
            subset.append(letter)
            tempwords=utils.filter_words_by_subset(''.join(subset), words)
            if len(tempwords)>maxes[i]:
                index=i2
                maxes[i]=len(tempwords)
                currentletter=letter
                wordlists[i]=tempwords
            subset.pop()
        subset.append(currentletter) 
        letters.pop(index)
    averages = [0.0]*len(maxes)
    for i, max in enumerate(maxes):
        averages[i]=max/(i+1)
    print("time taken: ", time.time()-start_time, "s")
    return subset, wordlists, maxes, averages
def find_good_letters_reverse(letters, words): 
    start_time=time.time()
    letters=list(letters)
    maxes=[-1]*len(letters)
    averages=[0.0]*len(letters)
    subset=['']*len(letters)
    currentletterindex=0
    maxes[len(letters)-1]=len(utils.filter_words_by_subset(''.join(letters),words) )
    for i in range(len(letters)):
        listsindex=len(letters)-1
        #print(listsindex, maxes[listsindex])
        for i2, letter in enumerate(letters):
            letters.pop(i2)
            tempwords=utils.filter_words_by_subset(''.join(letters),words) 
            if len(tempwords)>maxes[listsindex-1]:
                #print("current letter changed")
                currentletterindex=i2
                maxes[listsindex-1]=len(tempwords)
                subset[listsindex]=letter
            letters.insert(i2, letter)
        #print(i)
        #print(len(letters))
        #print(currentletterindex)
        if len(letters)>1:
            letters.pop(currentletterindex)
    subset[0]=letters[0]
    for i, max in enumerate(maxes):
        averages[i]=max/(i+1)
    print("Time taken: ", time.time()-start_time, "s")
    return subset, maxes, averages
