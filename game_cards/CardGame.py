from Card import Card       # ex.4
from DeckOfCards import DeckOfCards
from Player import Player


class CardGame:
    def __init__(self, name_1: str, name_2: str, num_of_cards_1: int, num_of_cards_2: int):
        self.player1 = Player(name_1, num_of_cards_1)
        self.player2 = Player(name_2, num_of_cards_2)
        self.deck = DeckOfCards()
        self.out_card = []  # קלפים שהוצאו מהמשחק
        self.new_game()

    def new_game(self):
        self.deck.cards_shuffle()
        len_deck = len(self.deck.cards)
        if len_deck == 52:  # check
            for i in range(len_deck):
                if self.player1.num_of_cards > len(self.player1.pack_cards):
                    self.player1.add_card(self.deck.deal_one())
                if self.player2.num_of_cards > len(self.player2.pack_cards):
                    self.player2.pack_cards.append(self.deck.deal_one())
        else:
            print("Error, not the beginning of the game")

    def get_winner(self):
        if len(self.player1.pack_cards) > len(self.player2.pack_cards):
            return self.player1
        if len(self.player2.pack_cards) > len(self.player1.pack_cards):
            return self.player2
        return None

    def __str__(self):
        return f"name: {self.player1.name} pack of cards: {self.player1.pack_cards}" \
               f"len of list: {len(self.player1.pack_cards)}\n" \
               f"name: {self.player2.name} pack of cards: {self.player2.pack_cards} " \
               f"len of list: {len(self.player1.pack_cards)}"

    # def __repr__(self):
    #     return f"name: {self.player1.name} pack of cards: {self.player1.pack_cards}\n" \
    #            f"name: {self.player2.name} pack of cards: {self.player2.pack_cards}"