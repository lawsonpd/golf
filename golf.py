import random
import itertools

def golf(hands):
    return allmax(hands, key=hand_score)

def allmax(hands):
    pass

def hand_score(hand):
    pass

def hand(k=4):
    "Returns a hand of k cards."
    pass

def deal():
    pass

def score_hand(hand):
    pass

def swap_card(hand, old_card, new_card):
    pass

def draw_pile():
    pass

def discard_pile():
    pass

player_turn = itertools.cycle(range(num_players))
# Could be something like the following
# (which doesn't work because it returns an iterator, which is not what we want):
# def player_turn(n=4):
#     turn = (itertools.cycle(range(n)))
#     yield turn

def test():
    pass
