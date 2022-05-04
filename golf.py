import random
import itertools

class Deck:
    def __init__(self):
        self.draw_pile = None
        self.discard_pile = None

    def deal_hands(self, hands):
        pass

class Hand:
    def __init__(self):
        self.cards = {} # Key, value: card, known/unknown

    def __gt__(self, value):
        # May use for comparisons in max/allmax
        pass

    def swap_card(self, new, old):
        pass

    def hand_score(self):
        return sum([v for v, s in self.cards])

def golf(hands):
    # return allmax(hands, key=hand_score)
    pass

def allmax(hands):
    pass

# player_turn = itertools.cycle(range(num_players))
# Could be something like the following
# (which doesn't work because it returns an iterator, which is not what we want):
# def player_turn(n=4):
#     turn = (itertools.cycle(range(n)))
#     yield turn

def test():
    pass
