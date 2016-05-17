from __future__ import division, print_function

import arguments
from Game import Game
from bots import *
from Player import Player


# Change these to edit the default Game parameters
DEFAULT_VERBOSITY = True
DEFAULT_MIN_ROUNDS = 1000
DEFAULT_AVERAGE_ROUNDS = 2000
DEFAULT_END_EARLY = False
#DEFAULT_PLAYERS = [Player(), Pushover(), Freeloader(), Alternator(), MaxRepHunter(), Random(.2), Random(.8), FairHunter(), AverageHunter(), Player(), Pushover(), Freeloader(), Alternator(), MaxRepHunter(), Random(.2), Random(.8), FairHunter(), AverageHunter(), Player(), Pushover(), Freeloader(), Alternator(), MaxRepHunter(), Random(.2), Random(.8), FairHunter(), AverageHunter()]
DEFAULT_PLAYERS = [Player(),NormalHunter(),NormalPlusHunter(),Freeloader(), 
MaxRepHunter(), FairHunter(), NormalHunter(),NormalPlusHunter(),
BoundedHunter(0.4,0.8),NormalHunter(),Freeloader(), NormalPlusHunter(),
MaxRepHunter(), FairHunter(), NormalHunter(),NormalPlusHunter(),
BoundedHunter(0.4,0.8),NormalHunter(),Freeloader(), NormalPlusHunter(),
MaxRepHunter(), FairHunter(), NormalHunter(),NormalPlusHunter(),
BoundedHunter(0.4,0.8)]
'''
DEFAULT_PLAYERS = [Player(),NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(), FairHunter(),MaxRepHunter(),BoundedHunter(0.4,0.9),Freeloader(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(), FairHunter(),MaxRepHunter(),BoundedHunter(0.5,0.7),Freeloader(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(), FairHunter(),MaxRepHunter(),BoundedHunter(0.5,0.8),Freeloader(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(), FairHunter(),MaxRepHunter(),BoundedHunter(0.4,0.8),Freeloader(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),NormalHunter(),NormalPlusHunter(), FairHunter(),MaxRepHunter(),BoundedHunter(0.4,0.8),Freeloader(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),NormalHunter(),NormalPlusHunter(), FairHunter(),MaxRepHunter(),BoundedHunter(0.4,0.8),Freeloader(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),NormalHunter(),NormalPlusHunter(), FairHunter(),MaxRepHunter(),BoundedHunter(0.4,0.8),Freeloader(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),NormalHunter(),NormalPlusHunter(), FairHunter(),MaxRepHunter(),BoundedHunter(0.4,0.8),Freeloader(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),NormalHunter(),NormalPlusHunter(), FairHunter(),MaxRepHunter(),BoundedHunter(0.4,0.8),Freeloader(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),NormalHunter(),NormalPlusHunter(), FairHunter(),MaxRepHunter(),BoundedHunter(0.4,0.8),Freeloader(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),NormalHunter(),NormalPlusHunter(), FairHunter(),MaxRepHunter(),BoundedHunter(0.4,0.8),Freeloader(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),NormalHunter(),NormalPlusHunter(), FairHunter(),MaxRepHunter(),BoundedHunter(0.4,0.8),Freeloader(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),NormalHunter(),NormalPlusHunter(), FairHunter(),MaxRepHunter(),BoundedHunter(0.4,0.8),Freeloader(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),NormalHunter(),NormalPlusHunter(), FairHunter(),MaxRepHunter(),BoundedHunter(0.4,0.8),Freeloader(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),NormalHunter(),NormalPlusHunter(), FairHunter(),MaxRepHunter(),BoundedHunter(0.4,0.8),Freeloader(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),NormalHunter(),NormalPlusHunter(), FairHunter(),MaxRepHunter(),BoundedHunter(0.4,0.8),Freeloader(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),NormalHunter(),NormalPlusHunter(), FairHunter(),MaxRepHunter(),BoundedHunter(0.4,0.8),Freeloader(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter(),
NormalHunter(),NormalPlusHunter()]'''
# Bare minimum test game. See README.md for details.

if __name__ == '__main__':
    (players, options) = arguments.get_arguments()
    # The list of players for the game is made up of
    #   'Player' (your strategy)
    #   bots from get_arguments (the bots to use)
    player_list = players
    # **options -> interpret game options from get_arguments
    #              as a dictionary to unpack into the Game parameters
    game = Game(player_list, **options)
    game.play_game()
