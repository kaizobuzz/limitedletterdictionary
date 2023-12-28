import utils
import time
def should_skip(letters):
    if all([x not in letters for x in "aeiou"]):
        return True
    if "q" in letters and not "u" in letters:
        return True
    return False

def find_optimal_letters(letters, words):  
    start_time=time.time()
    max = [0]*len(letters)
    solutions = [""]*len(letters)
    wordlists = [[]]*len(letters)
    subset = []
    count = [0]
    num_skipped = [0]
    def dfs(i):
        if i>=len(letters):
            count[0]+=1
            #just a printing statement
            if count[0]%10000==0:
                if count[0]%100000==0:
                    print("\n\n", wordlists, "\n\n")
                print(f"maxes: {max}, \n\nsolutions: {solutions} \n\nprogress: {count[0]/(2**26)}")
                print(f"time spent so far: {time.time()-start_time}s")
                print(f"Letters skipped: {num_skipped[0]} \n")
            if should_skip(letters):
                num_skipped[0] += 1
                return
            setlength=len(subset)-1
            subsetstr=''.join(subset)
            tempwords=utils.filter_words_by_subset(subsetstr, words)
            #something here to account for weights 
            if len(tempwords)>max[setlength]:
                solutions[setlength]=subsetstr
                max[setlength]=len(tempwords)
                wordlists[setlength]=tempwords
            return
        subset.append(letters[i])
        dfs(i+1)
        subset.pop()
        dfs(i+1)

    dfs(0)
    return solutions, wordlists
         


