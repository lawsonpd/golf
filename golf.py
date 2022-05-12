import random
import itertools

class Deck:
    def __init__(self):
        self.cards = [f'{r}{s}' for r in 'A23456789TJQK' for s in 'DHCS']
        random.shuffle(self.cards)
        self.draw_pile = self.cards
        self.discard_pile = []

    def deal_hands(self, *hands, k=4):
        for i in range(k):
            for hand in hands:
                hand.cards.append(self.cards.pop())

    def card_from_draw_pile(self):
        return self.draw_pile.pop()

    def card_from_discard_pile(self):
        return self.discard_pile.pop()

    def card_to_discard_pile(self, card):
        self.discard_pile.append(card)

class Hand:
    def __init__(self):
        self.cards = []

    def __lt__(self, other_hand) -> bool:
        # TODO Extract value components of cards, sort, and compare pairwise by index
        pass

    def __eq__(self, other_hand) -> bool:
        # TODO Extract value components of cards, sort, and compare pairwise by index
        pass

    def __repr__(self) -> str:
        return ' '.join(card for card in self.cards)

    def swap_card(self, new:str, i:int) -> str:
        "Assign card `new` at index `i` and return card previously at index `i`."
        discarded = self.cards[i]
        self.cards[i] = new
        return discarded

    def hand_score(self) -> int:
        return sum([v for v, s in self.cards])

def golf(hands):
    # return allmax(hands, key=hand_score)
    pass

def allmax(hands):
    pass

def sort_hand(hand):
    "Sort a hand by card ranks"
    pass

# player_turn = itertools.cycle(range(num_players))
# Could be something like the following
# (which doesn't work because it returns an iterator, which is not what we want):
# def player_turn(n=4):
#     turn = (itertools.cycle(range(n)))
#     yield turn

def test():
    pass
