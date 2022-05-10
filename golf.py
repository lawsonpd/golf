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

class Hand:
    def __init__(self):
        self.cards = []
        self.known_cards = {0,1}

    def __lt__(self, other_hand) -> bool:
        pass

    def __eq__(self, other_hand) -> bool:
        pass

    def __repr__(self) -> str:
        "Reveals only known cards in hand"
        cards = []
        for i in range(len(self.cards)):
            if i in self.known_cards:
                cards.append(self.cards[i])
            else:
                cards.append('X')
        return ' '.join(card for card in cards)

    def swap_card(self, new:str, old:int, deck) -> None:
        real_i = old-1 # Assume user gives indices starting at 1
        discarded = self.cards[real_i]
        self.cards[real_i] = new # Assign new card at given index
        self.known_cards.add(real_i) # Record that added card (index) is now known
        deck.discard_pile.append(discarded)

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
