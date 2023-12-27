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
        

def do_genetic_algorithm(wordlist, num_agents, iterations):
    # verify inputs
    if num_agents < 2:
        raise ValueError("too few agents")
    #thing
    def sorting_key(a):
        return len(utils.filter_words_by_subset(a.get_letter_list(), wordlist))
    # generate agents
    agents = []
    for _ in range(num_agents):
        agents.append(Agent())
    for iter_num in range(iterations):
        #sort agents by score
        agents.sort(key=sorting_key)
        #murder agents who underperform
        
        num_agents_to_murder = len(agents) // 2
        del agents[0:num_agents_to_murder-1]

        #modify well-performing agents
        new_agents = []
        for agent in agents:
            new_agents.append(copy.deepcopy(agent).mutate())
        agents += new_agents

        print(f"Finished iteration {iter_num}/{iterations} with {num_agents} agents")
    agents.sort(key=sorting_key)
    return agents[-1].get_letter_list()
