from __future__ import division
from Player import BasePlayer

import random
import math
import numpy

class Pushover(BasePlayer):
    '''Player that always hunts.'''
    def __init__(self):
        self.name = "Pushover"
    
    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        return ['h']*len(player_reputations)

        
class Freeloader(BasePlayer):
    '''Player that always slacks.'''
    
    def __init__(self):
        self.name = "Freeloader"
    
    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        return ['s']*len(player_reputations)
        

class Alternator(BasePlayer):
    '''Player that alternates between hunting and slacking.'''
    def __init__(self):
        self.name = "Alternator"
        self.last_played = 's'
        
    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        hunt_decisions = []
        for i in range(len(player_reputations)):
            self.last_played = 'h' if self.last_played == 's' else 's'
            hunt_decisions.append(self.last_played)

        return hunt_decisions

class MaxRepHunter(BasePlayer):
    '''Player that hunts only with people with max reputation.'''
    def __init__(self):
        self.name = "MaxRepHunter"

    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        threshold = max(player_reputations)
        return ['h' if rep == threshold else 's' for rep in player_reputations]


class Random(BasePlayer):
    '''
    Player that hunts with probability p_hunt and
    slacks with probability 1-p_hunt
    '''
    
    def __init__(self, p_hunt):
        assert p_hunt >= 0.00 and p_hunt <= 1.00, "p_hunt must be at least 0 and at most 1"
        self.name = "Random" + str(p_hunt)
        self.p_hunt = p_hunt

    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        return ['h' if random.random() < self.p_hunt else 's' for p in player_reputations]

class FairHunter(BasePlayer):
    '''Player that tries to be fair by hunting with same probability as each opponent'''
    def __init__(self):
        self.name = "FairHunter"

    def hunt_choices(
                self,
                round_number,
                current_food,
                current_reputation,
                m,
                player_reputations,
                ):
        return ['h' if random.random() < rep else 's' for rep in player_reputations]
        
class BoundedHunter(BasePlayer):
    '''Player that hunts whenever the other's reputation is within some range.'''
    def __init__(self,lower,upper):
        self.name = "BoundedHunter" + str(lower)+'-'+str(upper)
        self.low = lower
        self.up = upper

    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        return ['h' if self.low <= rep <= self.up else 's' for rep in player_reputations]
        
class AverageHunter(BasePlayer):
    '''Player that tries to maintain the average reputation, but spreads its hunts randomly.'''
    
    def __init__(self):
        self.name = "AverageHunter"

    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        avg_rep = sum(player_reputations) / float(len(player_reputations))
        return ['h' if random.random() < avg_rep else 's' for rep in player_reputations]
        
class NormalHunter(BasePlayer):
    
    def __init__(self):
        self.name = "NormalHunter"
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

        for reputation in player_reputations:
            if reputation < 0.2 or reputation > 0.9: #TODO do this only for rounds after e.g. round 5
                decision = 's' 
            else:
                hunt_probability = (1/(math.exp((((reputation-0.5)*4)**2))))
                choice = self.weighted_choice([hunt_probability, 1-hunt_probability])
                if choice == 0:
                    decision = 'h'
                else:
                    decision = 's'
            hunt_decisions.append(decision)  

        return hunt_decisions
        
class NormalPlusHunter(BasePlayer):

    def __init__(self):
        self.name = "NormalPlusHunter"
        self.hunters = list()
        self.food_earnings = list()
        self.award = list()
        self.m = list()

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
        '''Required function defined in the rules'''
        decision = 's'
        hunt_probability = 0            
        hunt_decisions = list()
        number_of_players = len(player_reputations) + 1
        max_m = number_of_players*(number_of_players-1)
        adjustment = 1
        choice = 0

        if m < numpy.average(self.hunters):
            adjustment += 0.1
        if current_reputation < numpy.mean(player_reputations):
            adjustment += numpy.mean(player_reputations)

        for reputation in player_reputations:
            if reputation < 0.2 or reputation > 0.9: #TODO do this only for rounds after e.g. round 5
                hunt_probability = 0
            else:
                hunt_probability = (1/(math.exp((((reputation-0.5)*4)**2))))
            hunt_probability *= adjustment
            if hunt_probability > 1:
                hunt_probability = 1
            choice = self.weighted_choice([hunt_probability, 1-hunt_probability])

            if choice == 0:
                decision = 'h'
            else:
                decision = 's'

            hunt_decisions.append(decision)  

        return hunt_decisions
        

    def hunt_outcomes(self, food_earnings):
        '''Required function defined in the rules'''
        self.food_earnings.append(sum(food_earnings))
        return
        
        

    def round_end(self, award, m, number_hunters):
        '''Required function defined in the rules'''
        self.hunters.append(number_hunters)
        self.award.append(award)
        self.m.append(m)
        return