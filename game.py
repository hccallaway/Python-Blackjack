from player import Player
from deck import Deck


def get_hand_str(person):
    hand = person.get_hand()
    hand_str = "[ "
    for i in range(0, len(hand)):
        hand_str += hand[i].to_string()
        if i < len(hand) - 1:
            hand_str += ", "
    hand_str += " ]"
    return hand_str


class Game:

    def __init__(self):
        self.player = Player()
        self.dealer = Player()
        self.deck = Deck()
        self.games_played = 0
        self.games_won = 0
        self.continue_answer = None

    def deal_new_hands(self):
        p_new_card = self.deck.deal()
        self.player.add_card(p_new_card)
        d_new_card = self.deck.deal()
        self.dealer.add_card(d_new_card)

    def dealer_play(self):
        while self.dealer.get_total() <= 17:
            new_card = self.deck.deal()
            self.dealer.add_card(new_card)

    def determine_winner(self):
        p_total = self.player.get_total()
        d_total = self.dealer.get_total()

        print("The dealer's cards are", get_hand_str(self.dealer), "for a total of", self.dealer.get_total())
        if p_total <= 21 < d_total or (p_total <= 21 and d_total <= 21 and 21 - p_total < 21 - d_total):
            print("You won!")
            self.games_won += 1
        elif d_total <= 21 < p_total or (p_total <= 21 and d_total <= 21 and 21 - d_total < 21 - p_total):
            print("The dealer won!")
        else:
            print("You tied with the dealer!")

    def end_game(self):
        self.games_played += 1
        print("Thanks for playing! So far you have won", self.games_won, "out of", self.games_played, "game(s)\n")
        self.continue_answer = input("Want to go again? (enter 'y' for yes or 'n' for no) ")
        self.player.new_hand()
        self.dealer.new_hand()

    def play(self):
        self.continue_answer = input("Do you want to play blackjack? (enter 'y' for yes or 'n' for no) ")

        while self.continue_answer == 'y':
            if len(self.player.get_hand()) == 0:
                for i in range(0, 2):
                    self.deal_new_hands()
                print("The dealer's one face-up card is", self.dealer.get_hand()[0].get_rank())
                print("The dealer is now playing their hand...")
                self.dealer_play()
                print("The dealer now has", len(self.dealer.get_hand()), "cards")

            print("Your cards are", get_hand_str(self.player), "for a total of", self.player.get_total())
            if 21 < self.player.get_total():
                print("Bust! Your hand went over 21")
                self.end_game()
                continue

            hit_answer = input("Do you want to hit or stand? (enter 'h' for hit or 's' for stand) ")

            if hit_answer == 'h':
                new_card = self.deck.deal()
                self.player.add_card(new_card)
                # if 21 < self.player.get_total():
                #     print("Bust! Your hand went over 21")
                #
                #     self.determine_winner()
                #     self.end_game()
                continue
            elif hit_answer == 's':
                self.determine_winner()
                self.end_game()
