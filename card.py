class Card:

    def __init__(self, rank):
        self.rank = rank

    def to_string(self):
        card_obj = {
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "10",
            11: "Jack",
            12: "Queen",
            13: "King",
            14: "Ace"
        }

        if self.rank in card_obj:
            return card_obj[self.rank]

    def get_rank(self):
        return self.rank
