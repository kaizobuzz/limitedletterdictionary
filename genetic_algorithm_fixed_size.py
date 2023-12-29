import utils
import random
import time
import copy

class FixedSizeAgent:
    def __init__(self, size, subset=None):
        self.size = size
        if subset is None:
            alphabet = utils.alphabet()
            subset = ""
            while len(subset) < self.size:
                subset += list(alphabet).pop(random.randint(0, len(alphabet) - 1))
        self.subset = list(subset)
        self.not_subset = list(filter(lambda x: x not in self.subset, utils.alphabet()))

    def get_letter_list(self):
        return "".join(self.subset)

    def mutate(self):
        if self.size == len(utils.alphabet()):
            return self
        
        letter_to_add = self.not_subset.pop(random.randint(0, len(self.not_subset) - 1))
        letter_to_remove = self.subset.pop(random.randint(0, len(self.subset) - 1))

        self.not_subset += letter_to_remove
        self.subset += letter_to_add
        return self

def do_genetic_algorithm(bitfields, num_agents, iterations, size):
    cache_capacity=500
    min_agents = 2
    start_time = time.time()
    # verify inputs
    if num_agents < min_agents:
        raise ValueError("too few agents")
    #thing
    cache=utils.LRUCache(cache_capacity)
    def sorting_key(a):
        return utils.get_num_of_words_by_subset_with_cache(cache, a.get_letter_list(), bitfields) / len(a.get_letter_list())
    best_score=0
    best_letters=""
    # generate agents
    agents = []
    for _ in range(num_agents):
        agents.append(FixedSizeAgent(size))
    for iter_num in range(iterations):
        iteration_start_time=time.time()
        #sort agents by score
        agents.sort(key=sorting_key, reverse=True)
        
        best_score = sorting_key(agents[0])
        best_letters = agents[0].get_letter_list()

        #murder random agents, more likely to murder underperforming ones
        agents_to_remove = []
        for i in range(len(agents)):
            if random.random() > (1-i/num_agents):
                agents_to_remove.append(agents[i])
        for agent in agents_to_remove:
            agents.remove(agent)
        
        #refill array
        new_agents = []
        num_new_agents_needed = num_agents - len(agents)
        print(num_new_agents_needed)
        while num_new_agents_needed > 0:
            new_agents.append(copy.deepcopy(random.choice(agents)).mutate())
            num_new_agents_needed -= 1
        agents += new_agents

        print(f"Finished iteration {iter_num}/{iterations} with {num_agents} agents. \nbest score so far: {best_score}, with letters {best_letters}")
        print(f"Time since start: {time.time()-start_time}s")
        print(f"Time since last iteration: {time.time()-iteration_start_time}s")
    agents.sort(key=sorting_key, reverse=True)
    return agents[0].get_letter_list()
