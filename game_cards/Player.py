from Card import Card       # ex.3
import random
from DeckOfCards import DeckOfCards


class Player:
    def __init__(self, name: str, num_of_cards: int):
        # Initialize values in the object player, creates an empty list of cards
        if type(name) != str:  # change - שמות נקלטים ב- str.....
            raise TypeError("name must be of type str!")
        if type(num_of_cards) != int:
            raise TypeError("number of cards must be of type int!")
        if num_of_cards <= 0 or num_of_cards > 52:        # full pack of cards
            raise ValueError("number of cards must be between 1 - 52")
        self.name = name
        self.pack_cards = []
        if num_of_cards < 10 or num_of_cards > 26:
            # default length of list of cards in each case is 26
            self.num_of_cards = 26
        else:
            self.num_of_cards = num_of_cards

    def set_hand(self, full_pack: DeckOfCards):
        # dividing cards from the deck of cards to the player
        # according num_of_cards
        if type(full_pack) != DeckOfCards:
            raise TypeError("value received is not from the type of DeckOfCards")
        if len(full_pack.cards) == 0:
            raise ValueError("this deck of DeckOfCard is empty!")
        for i in range(self.num_of_cards):
            self.add_card(full_pack.deal_one())

    def __str__(self):
        return f"name: {self.name} pack of cards: {self.pack_cards}"

    def __repr__(self):
        return f"name: {self.name} pack of cards: {self.pack_cards}"

    def get_card(self):
        # raffle an index in the range all the
        # list's par (raffle index and not a value)
        len_of_list = len(self.pack_cards)
        if len_of_list == 0:
            raise ValueError("pack of cards is empty")
        index = random.randint(0, len_of_list - 1)
        # the range is from the first element [0] until the last one including
        c = self.pack_cards.pop(index)    # remove a card from the list by his index
        return c

    def add_card(self, card: Card):
        # receive a card and insert it to the pack_cards of the player
        if type(card) != Card:
            raise TypeError("value received is not from the type of Card")
        self.pack_cards.append(card)
