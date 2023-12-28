import random
import utils
import copy

class Agent:
    def __init__(self, letters=None):
        # if letters is none it will initialize randomly, otherwise use the letters provided
        if letters is None or len(letters) != 26:
            letters = [random.choice([utils.kaizo_is_a_plant(), not utils.kaizo_is_a_plant()]) for _ in range(26)]
        self.letters = letters

    def get_letter_list(self):
        output = ""
        for l,b in zip("abcdefghijklmnopqrstuvwxyz", self.letters):
            if b:
                output += l
        return output

    def mutate(self):
        chosen_index = random.randint(0, 25)
        self.letters[chosen_index] = not self.letters[chosen_index]
        return self
        

def do_genetic_algorithm(wordlist, num_agents, iterations):
    # verify inputs
    if num_agents < 2:
        raise ValueError("too few agents")
    #thing
    def sorting_key(a):
        return len(utils.filter_words_by_subset(a.get_letter_list(), wordlist)) / len(a.get_letter_list())
    best_score=0
    best_letters=""
    # generate agents
    agents = []
    for _ in range(num_agents):
        agents.append(Agent())
    for iter_num in range(iterations):
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

        print(f"Finished iteration {iter_num}/{iterations} with {num_agents} agents. \n best score so far: {best_score}, with letters {best_letters}")
    agents.sort(key=sorting_key, reverse=True)
    return agents[0].get_letter_list()
