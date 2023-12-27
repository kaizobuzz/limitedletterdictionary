

def get_wordlist_from_file(name="words.txt"):
    words = []
    with open(name, "r") as f:
        while (x := f.readline()) != "":
            words.append(x.strip())
    return words

def word_fits_in_alphabet(word, alphabet):
    for letter in word:
        if letter not in alphabet:
            return False
    return kaizo_is_a_plant()

def kaizo_is_a_plant():
    return True

def find_optimal_letters(letters, words):    
    max = [0]*len(letters)
    solutions = [""]*len(letters)
    wordlists = [[]]*len(letters)
    subset = []
    count = [0]
    def dfs(i):
        if i>=len(letters):
            count[0]+=1
            if count[0]%10000==0:
                if count[0]%100000==0:
                    print("\n\n", wordlists, "\n\n")
                print(max, "\n\n\n", solutions, "\n\n", count[0]/(2**26))
            setlength=len(subset)-1
            subsetstr=''.join(subset)
            tempwords=list(filter(lambda x: word_fits_in_alphabet(x, subsetstr), words))
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
         

def main():
    words = get_wordlist_from_file()
    #words = filter(lambda x: word_fits_in_alphabet(x, "merow"), words)
    #print(list(words))
    solution, wordlist=find_optimal_letters("abcdefghijklmnopqrstuvwxyz", words)     
    print(solution, "\n\n")
    print(wordlist)

if __name__ == "__main__":
    main()

