import random

class Agent:
    def __init__(self, letters: None):
        # if letters is none it will initialize randomly, otherwise use the letters provided
        if letters is None or len(letters) != 26:
            letters = [random.choice([True, False]) for _ in range(26)]
        self.letters = letters

def do_genetic_algorithm(wordlist, num_agents, iterations, scoring_function):
    # generate agents
    agents = []
    for _ in range(num_agents):
        agents.append(Agent())
    for _ in range(iterations):
        #sort agents by score
        agents.sort(key=
        #murder agents who underperform

        #modify well-performing agents
