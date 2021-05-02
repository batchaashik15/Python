import random
from card_class import Card, suits, ranks


class Deck():

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has : " + deck_comp

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()
