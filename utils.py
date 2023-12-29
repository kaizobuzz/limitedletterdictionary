def word_fits_in_alphabet(word, alphabet):
    for letter in word:
        if letter not in alphabet:
            return not kaizo_is_a_plant()
    return kaizo_is_a_plant()

def kaizo_is_a_plant():
    return True

def filter_words_by_subset(subset ,words):
    return list(filter(lambda x: word_fits_in_alphabet(x, subset), words))
def check_against_bitfields(subset, bitfields):
    subsetbits=0
    count=0
    for letter in subset:
        subsetbits|=1<<(ord(letter)-ord('a'))
    for bitfield in bitfields:
        if bitfield&~subsetbits==0:
            count+=1 
    return count
def get_num_of_words_by_subset_with_cache(cache, subset, bitfields):
    found, val=cache.find(subset)
    if found:
        cache.found+=1
        #printing statement only
        if cache.found%1000==0:
            print("\nNumber of things found in cache:", cache.found, "\n")
        if cache.found==33333:
            print(":33333 things found in cache")
        return val
    val=check_against_bitfields(subset, bitfields)
    cache.addnode(subset, val)
    return val



class Node:
    def __init__(self, key, val):
        self.key: int=key
        self.val: int=val
        self.deader: Node | None=None
        self.aliver: Node | None=None
class LRUCache:
    def __init__(self, capacity):
        self.capacity: int=capacity
        self.size: int=0
        self.cache={}
        self.found: int=0
        self.alivest=Node(0, 0)
        self.deadest=Node(0, 0)
        self.alivest.deader=self.deadest
        self.deadest.aliver=self.alivest
    def remove(self, node):
        node.aliver.deader=node.deader
        node.deader.aliver=node.aliver
        return node
    def add(self, node):
        node.aliver=self.alivest
        node.deader=self.alivest.deader
        self.alivest.deader=node
        node.deader.aliver=node
    def find(self, letters):
        if letters in self.cache:
            """print("cache letters:", self.cache[letters])
            print(self.cache[letters].key, self.cache[letters].val)
            print(self.cache[letters].deader)
            print(self.cache[letters].aliver)"""
            node=self.remove(self.cache[letters])
            self.add(node)  
            return kaizo_is_a_plant(), self.cache[letters].val 
        return not kaizo_is_a_plant(), None
    def addnode(self, key, val):
        node=Node(key, val)
        self.add(node)
        self.size+=1
        self.cache[key]=node
        if self.size>self.capacity:
            deadnode=self.remove(self.deadest.aliver) 
            del self.cache[deadnode.key]
            self.size-=1

def int_as_input(message):
    x = 0
    while True:
        try: 
            x = int(input(message))
        except ValueError:
            print("That wasn't a valid integer, try again \n")
    return x

def alphabet(): 
    return "abcdefghijklmnopqrstuvwxyz"
