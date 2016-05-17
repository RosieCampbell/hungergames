# Based on Chad Miller's testing Framework

import random
import math
import numpy

class BasePlayer(object):
    '''
    Base class so I don't have to repeat bookkeeping stuff.
    Do not edit unless you're working on the simulation.
    '''
    
    def __str__(self):
        try:
            return self.name
        except AttributeError:
            # Fall back on Python default
            return super(BasePlayer, self).__repr__()
    
    def hunt_choices(*args, **kwargs):
        raise NotImplementedError("You must define a strategy!")
        
    def hunt_outcomes(*args, **kwargs):
        pass
        
    def round_end(*args, **kwargs):
        pass

class Player(BasePlayer):

    def __init__(self):
        self.max_m = 0
        self.name = "Rosie"
        self.huntProportion = list()
    

    # Returns each list index with the probability of its value
    def weighted_choice(self, weights):
        totals = []
        running_total = 0

        for w in weights:
            running_total += w
            totals.append(running_total)

        rnd = random.random() * running_total
        for i, total in enumerate(totals):
            if rnd < total:
                return i

    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
   
        decision = 's'
        hunt_probability = 0            
        hunt_decisions = list()
        number_of_players = len(player_reputations) + 1
        self.max_m = number_of_players*(number_of_players-1)
        adjustment = 1
        choice = 0

	# More likely to hunt if m is small. Checks average proportion of hunts relative to interactions over the whole game.
	# If m is less than it, hunt_probability will be adjusted by multiplying by a factor of 1.1
        if len(self.huntProportion) > 0:
            if m/float(self.max_m) < numpy.mean(self.huntProportion):
                adjustment += 0.1

        for reputation in player_reputations:

	    # Calculates the hunt probability based on a gaussian distribution. If the opponent's reputation is very low or very high, my probability of hunting will be low. My probability of hunting peaks around the center values.
            hunt_probability = 1.0/(math.exp((((reputation-0.5)*4)**2)))

	    # Weights the gaussian to favour higher reputations
            hunt_probability = (hunt_probability + reputation)/2.0

	    # Ensures my reputation doesn't fall too low by aggresively increasing my hunt probability when my reputation falls below 0.5
            if current_reputation < 0.5:
                hunt_probability += 0.5 - current_reputation

	    # No point hunting with players that will almost certainly slack or almost certainly hunt, so probability of hunting at these extremes is set to 0. Only applies after the tenth round to give players a chance to build up a representative reputation
            elif round_number > 10 and (reputation < 0.2 or reputation > 0.9): 
                hunt_probability = 0
	    # Applies the adjustment for small m if applicable
            hunt_probability *= adjustment  

	    # Caps the hunt probability at 1         
            if hunt_probability > 1:
                hunt_probability = 1

	    # Sends the probabilities to a function which returns a weighted random value
            choice = self.weighted_choice([hunt_probability, 1-hunt_probability])

	    # Depending on the outcome, set the decision to 'h' or 's'
            if choice == 0:
                decision = 'h'
            else:
                decision = 's'

            hunt_decisions.append(decision)  

        return hunt_decisions
        

    def hunt_outcomes(self, food_earnings):
        pass
        

    def round_end(self, award, m, number_hunters):
	# Keeps track of the proportion of 'hunt' decisions over entire game
        self.huntProportion.append(number_hunters/float(self.max_m))
        return
        

