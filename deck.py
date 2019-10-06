from card import Card
import random


def get_cards():
    cards = []

    for suit in range(0, 4):  # 4 suits
        for rank in range(2, 15):  # 13 cards/suit
            cards.append(Card(rank))

    random.shuffle(cards)
    return cards


class Deck:

    def __init__(self):
        self.cards = get_cards()
        self.top = 0

    def deal(self):
        if self.top == len(self.cards) - 1:
            random.shuffle(self.cards)
            self.top = 0
        card = self.cards[self.top]
        self.top += 1
        return card
