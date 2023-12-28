import utils
import time
def should_skip(letters):
    if all([x not in letters for x in "aeiou"]):
        return True
    if "q" in letters and not "u" in letters:
        return True
    return False

def find_optimal_letters(letters, bitfields):  
    start_time=time.time()
    maxes = [0]*len(letters)
    averages = [0.0]*len(letters)
    solutions = [""]*len(letters)
    subset = []
    count = [0]
    num_skipped = [0]
    def dfs(i):
        if i>=len(letters):
            count[0]+=1
            #just a printing statement
            if count[0]%10000==0: 
                print(f"maxes: {maxes}, \n\nsolutions: {solutions} \n\nprogress: {(count[0]/(2**26))*100}%")
                print(f"time spent so far: {time.time()-start_time}s")
                print(f"Letters skipped: {num_skipped[0]} \n")
            if should_skip(letters):
                num_skipped[0] += 1
                return
            setlength=len(subset)-1
            subsetstr=''.join(subset)
            tempwords=utils.check_against_bitfields(subsetstr, bitfields)
            #something here to account for weights 
            if tempwords>maxes[setlength]:
                solutions[setlength]=subsetstr
                maxes[setlength]=tempwords
            return
        subset.append(letters[i])
        dfs(i+1)
        subset.pop()
        dfs(i+1)

    dfs(0)
    for i, max in enumerate(maxes):
        averages[i]=max/(i+1)
    return solutions, maxes, averages
         


