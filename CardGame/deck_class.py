import card_class
from card_class import Card
import random


class Deck:
    '''
    Deck class to shuffle and have all the Crad objects in a list
    '''

    def __init__(self):
        self.all_cards = []

        for suit in card_class.suits:
            for rank in card_class.ranks:
                # Create the card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()
