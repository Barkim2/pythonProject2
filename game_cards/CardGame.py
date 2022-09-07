from DeckOfCards import DeckOfCards     # ex.4
from Player import Player


class CardGame:
    def __init__(self, name_1: str, name_2: str, num_of_cards_1: int, num_of_cards_2: int):
        if type(name_1) != str:
            raise TypeError("name of player_1 must be of type of string!")
        if type(name_2) != str:
            raise TypeError("name of player_2 must be of type of string!")
        if type(num_of_cards_1) != int:
            raise TypeError("number of cards of player_1 must be of type int!")
        if type(num_of_cards_2) != int:
            raise TypeError("number of cards of player_2 must be of type int!")
        if num_of_cards_1 > 26 or num_of_cards_1 <= 0:
            # 26 is half of pack of cards, 0 is the minimum amount of cards a player can have
            raise ValueError("number of cards must be between 0 - 26")
        if num_of_cards_2 > 26 or num_of_cards_2 <= 0:
            raise ValueError("number of cards must be between 0 - 26")
        self.player1 = Player(name_1, num_of_cards_1)
        self.player2 = Player(name_2, num_of_cards_2)
        self.deck = DeckOfCards()  # check
        self.new_game()     # mock

    def new_game(self):
        self.deck.cards_shuffle()
        len_deck = len(self.deck.cards)
        print(len_deck)
        if len_deck == 52:  # check
            for i in range(len_deck):
                if self.player1.num_of_cards > len(self.player1.pack_cards):
                    self.player1.add_card(self.deck.deal_one())
                if self.player2.num_of_cards > len(self.player2.pack_cards):
                    self.player2.pack_cards.append(self.deck.deal_one())
        else:
            print("Error, not the beginning of the game")
            return False

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
