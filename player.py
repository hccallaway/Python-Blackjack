class Player:

    def __init__(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def new_hand(self):
        self.hand = []

    def get_hand(self):
        return self.hand

    def get_total(self):
        total = 0
        for i in range(0, len(self.hand)):
            if self.hand[i].get_rank() < 11: # number card
                total += self.hand[i].get_rank()
            elif 11 <= self.hand[i].get_rank() <= 13: # face card, not ace
                total += 10
            else: # ace
                if total + 11 <= 21: # high
                    total += 11
                else: # low
                    total += 1
        return total
