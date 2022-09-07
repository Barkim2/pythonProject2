from Card import Card       # ex.3
import random
from DeckOfCards import DeckOfCards


class Player:
    def __init__(self, name: str, num_of_cards: int):
        # Initialize values in the object player, creates an empty list of cards
        self.name = name
        self.pack_cards = []
        if num_of_cards < 10 or num_of_cards > 26:
            # default length of list of cards in each case is 26
            self.num_of_cards = 26
        self.num_of_cards = num_of_cards

    def set_hand(self, full_pack: DeckOfCards):
        # dividing cards from the deck of cards to the player
        # according num_of_cards
        for i in range(self.num_of_cards):
            self.pack_cards.append(full_pack.deal_one())

    def __str__(self):
        return f"name: {self.name} pack of cards: {self.pack_cards}"

    def __repr__(self):
        return f"name: {self.name} pack of cards: {self.pack_cards}"

    def get_card(self):
        len_of_list = len(self.pack_cards)
        index = random.randint(1, len_of_list - 1)
        c = self.pack_cards.pop(index)
        return c

    def add_card(self, card: Card):
        # receive a card and insert it to the pack_cards of the player
        self.pack_cards.append(card)
